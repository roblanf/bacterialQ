#!/usr/bin/env Rscript

library(readr)
library(stringr)
library(dplyr)
library(ggplot2)
library(patchwork)
options(repr.plot.width = 10, repr.plot.height = 10, repr.plot.res = 100)

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 4) {
  stop("Please provide exactly four arguments: subtree_iqtree, subtree_log, model_log, output_folder")
}

subtree_iqtree <- args[1]
subtree_log <- args[2]
model_log <- args[3]
output_folder <- args[4]

# Function to read a file and remove NUL characters
read_file_without_nul <- function(file_path) {
  r = readBin(file_path, raw(), file.info(file_path)$size)
  r[r==as.raw(0)] = as.raw(0x20) ## replace with 0x20 = <space>
  writeBin(r, file_path)
  lines = readLines(file_path)
  return(lines)
}

# Function to read and process iqtree file
process_subtree_iqtree <- function(file_path) {
  lines <- read_file_without_nul(file_path)

  # Identify the start and end lines for each table
  start_alignment_info <- which(str_detect(lines, "^Input data: ")) + 1
  end_alignment_info <- which(str_detect(lines, "^Column meanings:")) - 1
  start_subtree_info <- which(str_detect(lines, "^List of best-fit models per partition:")) + 1
  end_subtree_info <- which(str_detect(lines, "^AIC, w-AIC   : Akaike information criterion scores and weights.")) - 1

  # Extract the lines for each table
  alignment_info_lines <- lines[start_alignment_info:end_alignment_info]
  subtree_info_lines <- lines[start_subtree_info:end_subtree_info]

  # Replace " + ", " - " with " " in subtree_info_lines
  subtree_info_lines <- str_replace_all(subtree_info_lines, " \\+ ", " ")
  subtree_info_lines <- str_replace_all(subtree_info_lines, " \\- ", " ")

  # Read the tables
  alignment_info <- read_table(alignment_info_lines, col_names = TRUE)
  subtree_info <- read_table(subtree_info_lines, col_names = TRUE)

  # Join the tables
  joined_subtree_info <- left_join(alignment_info, subtree_info, by = "ID")

  # Select the desired columns
  joined_subtree_info <- select(joined_subtree_info, Seq, Site, Unique, Infor, Invar, Const, Name, Model, LogL) %>%
    rename(alignment = Name, logl_s = LogL, seq = Seq, site = Site, unique = Unique, infor = Infor, invar = Invar, const = Const, model_setting = Model)

  # Extract model name from model_setting
  joined_subtree_info <- mutate(joined_subtree_info, model = ifelse(str_detect(model_setting, "\\+"), str_extract(model_setting, "^[^\\+]+"), model_setting))

  # Extract ID from alignment
  joined_subtree_info <- joined_subtree_info %>%
    mutate(
      subtree_id = str_extract(alignment, "(?<=subtree_)\\d+(?=_)"),
      loci_id = str_extract(alignment, "(?<=subtree_)\\d+_[^.]+(?=\\.)")
  ) %>% 
    mutate(loci_id = str_remove(loci_id, "^\\d+_"))
  return(joined_subtree_info)
}

process_subtree_log <- function(subtree_log) {
  # Process subtree log
  lines <- read_file_without_nul(subtree_log)
  start_line <- tail(grep("Estimate model parameters \\(epsilon = [0-9.]+\\)", lines), 1) + 1
  end_line <- grep("Total number of iterations: 0", lines) - 1
  content <- lines[start_line:end_line]
  total_likelihood <- str_extract(content[length(content) - 4], "-?\\d+(\\.\\d+)?(E-?\\d+)?") %>% as.numeric()
  total_tree_length <- str_extract(content[length(content) - 1], "-?\\d+(\\.\\d+)?(E-?\\d+)?") %>% as.numeric()
  tibble_data <- content[1:(length(content) - 4)] %>%
    str_split(" / ", simplify = TRUE) %>%
    as_tibble(.name_repair = "unique") # Ensure unique column names

  # Directly assign column names
  colnames(tibble_data) <- c("alignment", "model", "df", "logl_s")
  tibble_data$alignment <- str_remove(tibble_data$alignment, "Partition ")
  tibble_data$model <- str_remove(tibble_data$model, "Model: ")
  tibble_data$df <- as.numeric(str_extract(tibble_data$df, "\\d+"))
  tibble_data$logl_s <- as.numeric(str_extract(tibble_data$logl_s, "-?\\d+(\\.\\d+)?E?-?\\d*"))

  return(tibble_data)
}

# Function to read and process model log
process_model_log <- function(file_path) {
  lines <- read_file_without_nul(file_path)
  log_likelihood_lines <- grep("\\d+\\. Log-likelihood:", lines)
  start_line <- log_likelihood_lines[length(log_likelihood_lines) - 1] + 3
  end_line <- log_likelihood_lines[length(log_likelihood_lines)] - 1
  content <- lines[start_line:end_line]
  total_likelihood <- str_extract(content[length(content) - 2], "-?\\d+(\\.\\d+)?(E-?\\d+)?") %>% as.numeric()
  total_tree_length <- str_extract(content[length(content) - 1], "-?\\d+(\\.\\d+)?(E-?\\d+)?") %>% as.numeric()
  tibble_data <- content %>%
    str_split(" / ", simplify = TRUE) %>%
    as_tibble(.name_repair = "unique") # Ensure unique column names

  # Directly assign column names
  colnames(tibble_data) <- c("alignment", "model", "df", "logl_m")

  tibble_data$alignment <- str_remove(tibble_data$alignment, "Partition ")
  tibble_data$model <- str_remove(tibble_data$model, "Model: ")
  tibble_data$df <- as.numeric(str_extract(tibble_data$df, "\\d+"))
  tibble_data$logl_m <- as.numeric(str_extract(tibble_data$logl_m, "-?\\d+(\\.\\d+)?E?-?\\d*"))
  log_info_model <- list(total_likelihood = total_likelihood, total_tree_length = total_tree_length, subtree_info = tibble_data)

  return(log_info_model)
}

# Process files
subtree_info <- process_subtree_iqtree(subtree_iqtree) %>% select(-logl_s)
subtree_ll_info <- process_subtree_log(subtree_log) %>% select(alignment, logl_s)
subtree_info <- left_join(subtree_info, subtree_ll_info, by = "alignment")
model_info <- process_model_log(model_log)

# Compare and plot
model_partition_table <- model_info$subtree_info %>% select(alignment, logl_m)
diff_partition_table <- left_join(subtree_info, model_partition_table, by = "alignment")
diff_partition_table <- diff_partition_table %>% mutate(ll_diff = logl_m - logl_s)

# Save the diff_partition_table
dir.create(output_folder, recursive = TRUE)
write_csv(diff_partition_table, file.path(output_folder, "model_update_detail.csv"))

# Filter the models with less than 10 alignments
filtered_diff_partition_table <- diff_partition_table %>%
  group_by(model) %>%
  filter(n() >= 10) %>%
  ungroup()

# Plot 1: ll_diff distribution with density
ll_diff_density <- filtered_diff_partition_table %>%
  filter(abs(ll_diff) <= quantile(abs(ll_diff), 0.99)) %>%
  ggplot(aes(x = ll_diff)) +
  geom_density(alpha = 0) + # Add density line without fill to ensure smooth density curve
  labs(
    title = "Distribution of Log-Likelihood Differences",
    x = "Log-Likelihood Difference (ll_diff)",
    y = "Density"
  ) +
  theme_minimal() +
  annotate("text",
    x = -Inf, y = Inf, label = paste0("Below 0: ", round(mean(diff_partition_table$ll_diff < 0) * 100, 2), "%"),
    hjust = -0.1, vjust = 1.1, color = "blue", size = 5
  ) +
  annotate("text",
    x = Inf, y = Inf, label = paste0("Above 0: ", round(mean(diff_partition_table$ll_diff > 0) * 100, 2), "%"),
    hjust = 1.1, vjust = 1.1, color = "red", size = 5
  )

# Plot 2: ll_diff by initial model, keeping only values within 98th percentile
ll_diff_by_model <- filtered_diff_partition_table %>%
  filter(abs(ll_diff) <= quantile(abs(ll_diff), 0.99)) %>%
  ggplot(aes(x = ll_diff, color = model)) +
  geom_density() +
  labs(
    title = "Log-Likelihood Difference by Initial Model",
    x = "Log-Likelihood Difference (ll_diff)",
    y = "Density"
  ) +
  theme_minimal()

density_plot <- ll_diff_density / ll_diff_by_model + plot_layout(heights = c(1, 1))

# Plot 3: Seq ~ ll_diff scatter plot with spline fit, and Infor ~ ll_diff below
seq_ll_diff <- ggplot(filtered_diff_partition_table, aes(x = seq, y = ll_diff, color = model)) +
  geom_smooth(method = "gam", formula = y ~ s(x, bs = "cs"), se = FALSE, linetype = "dashed", alpha = 0.2) +
  geom_point(alpha = 0.5) +
  labs(
    title = "Number of Sequences vs Log-Likelihood Change",
    x = "Number of Sequences (seq)",
    y = "Log-Likelihood Difference (ll_diff)"
  ) +
  theme_minimal()

infor_ll_diff <- ggplot(filtered_diff_partition_table, aes(x = infor, y = ll_diff, color = model)) +
  geom_smooth(method = "gam", formula = y ~ s(x, bs = "cs"), se = FALSE, linetype = "dashed", alpha = 0.2) +
  geom_point(alpha = 0.5) +
  labs(
    title = "Informative Sites vs Log-Likelihood Change",
    x = "Number of Informative Sites (infor)",
    y = "Log-Likelihood Difference (ll_diff)"
  ) +
  theme_minimal()

aln_size_plot <- seq_ll_diff / infor_ll_diff

# Plot 4: ll_diff by subtree_id boxplot plot
diff_partition_table_subtree <- diff_partition_table %>%
  group_by(subtree_id) %>%
  filter(n() > 4) %>%
  ungroup()

ll_diff_by_subtree <- ggplot(diff_partition_table_subtree, aes(x = reorder(as.factor(subtree_id), ll_diff, FUN = mean), y = ll_diff)) +
  geom_boxplot(outlier.shape = NA) +
  stat_summary(fun = mean, geom = "point", shape = 20, size = 3, color = "red") +
  geom_jitter(width = 0.2, alpha = 0.2) + 
  labs(
    title = "Log-Likelihood Difference by Subtree ID",
    x = "Subtree ID",
    y = "Log-Likelihood Difference (ll_diff)"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Set the width and height based on the number of unique subtree_id
subtree_count <- diff_partition_table %>%
  count(subtree_id) %>% filter(n > 5) %>% nrow()

# Plot 5: ll_diff by model violin plot
ll_diff_by_model_violin <- ggplot(diff_partition_table, aes(x = reorder(model, ll_diff, FUN = mean), y = ll_diff)) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "black") +
  geom_violin() +
  stat_summary(fun = mean, geom = "point", shape = 20, size = 3, color = "red") +
  labs(
    title = "Log-Likelihood Difference by Model",
    x = "Model",
    y = "Log-Likelihood Difference (ll_diff)"
  ) +
  theme_minimal()

# Plot 6: Stacked bar plot for model preference by subtree
subtree_model_stack_plot <- diff_partition_table_subtree %>%
  group_by(subtree_id, model) %>%
  summarise(count = n(), .groups = 'drop') %>%
  group_by(subtree_id) %>%
  mutate(prop = count / sum(count)) %>%
  ungroup() %>%
  mutate(subtree_id = factor(subtree_id, levels = diff_partition_table %>%
                               count(subtree_id, sort = TRUE) %>%
                               pull(subtree_id)),
         model = factor(model, levels = diff_partition_table %>%
                          count(model, sort = TRUE) %>%
                          pull(model))) %>%
  ggplot(aes(x = subtree_id, y = prop, fill = model)) +
  geom_bar(stat = "identity", position = "fill") +
  labs(
    title = "Model Preference by Subtree",
    x = "Subtree ID",
    y = "Proportion",
    fill = "Model"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Plot for loci_id ~ model
loci_model_stack_plot <- diff_partition_table %>%
  group_by(loci_id, model) %>%
  summarise(count = n(), .groups = 'drop') %>%
  group_by(loci_id) %>%
  mutate(prop = count / sum(count)) %>%
  ungroup() %>%
  mutate(loci_id = factor(loci_id, levels = diff_partition_table %>%
                            count(loci_id, sort = TRUE) %>%
                            pull(loci_id)),
         model = factor(model, levels = diff_partition_table %>%
                          count(model, sort = TRUE) %>%
                          pull(model))) %>%
  ggplot(aes(x = loci_id, y = prop, fill = model)) +
  geom_bar(stat = "identity", position = "fill") +
  labs(
    title = "Model Preference by Loci",
    x = "Loci ID",
    y = "Proportion",
    fill = "Model"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Combine the two plots using patchwork
model_preference_plot <- subtree_model_stack_plot / loci_model_stack_plot

# Save plots
ggsave(file.path(output_folder, "density_plot.png"), density_plot, width = 10, height = 10, dpi = 100, bg = "white")
ggsave(file.path(output_folder, "aln_size_plot.png"), aln_size_plot, width = 10, height = 10, dpi = 100, bg = "white")
ggsave(file.path(output_folder, "diff_by_model.png"), ll_diff_by_model_violin, width = 10, height = 10, dpi = 100, bg = "white")
ggsave(file.path(output_folder, "diff_by_subtree.png"), plot = ll_diff_by_subtree, width = 2 + (subtree_count / 3), height = 10, bg = "white", limitsize = FALSE)
ggsave(file.path(output_folder, "model_preference_plot.png"), model_preference_plot, width = 30, height = 10, dpi = 100, bg = "white")
