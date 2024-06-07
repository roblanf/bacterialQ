library(tidyverse)
library(fs)

# Function to convert markdown table content to tibble
markdown_table_to_tibble <- function(table_content) {
  table_content <- table_content[-2]
  table_content <- gsub("^\\| | \\|$", "", table_content)
  table_content <- paste(table_content, collapse = "\n")
  table <- read_delim(table_content, delim = "|", trim_ws = TRUE, show_col_types = FALSE)
  return(table)
}

# Function to process concatenated test tables
process_concat_test_tables <- function(log_list) {
  concat_test_tables <- map(log_list, ~ {
    file_content <- read_lines(.x)
    test_lines <- grep("^### Final model testing of concatenated test loci  ", file_content)
    start_line <- test_lines + which(file_content[test_lines:length(file_content)] == "| Model | LogL | BIC |")[1] - 1
    end_line <- grep("^### PCA Plot for all models  ", file_content) - 1
    table_content <- file_content[start_line:end_line]
    table <- markdown_table_to_tibble(table_content)
    table$test <- gsub("\\_log.md$", "", basename(.x))
    table <- table %>%
      rename(model_string = Model) %>%
      mutate(
        model_type = ifelse(str_detect(model_string, "^[a-zA-Z]__.*"), "trained", "existed"),
        F_type = ifelse(str_detect(model_string, "\\+F"), "FE", "FO"),
        max_tree_size = as.numeric(str_extract(test, "\\d+$"))
      ) %>%
      mutate(model = str_extract(model_string, "^[^+]*"))
    return(table)
  })
  concat_test_sum <- concat_test_tables %>% bind_rows()
  return(concat_test_sum)
}

# Function to process initial model tables
process_initial_model_tables <- function(log_list) {
  initial_model_tables <- map(log_list, ~ {
    file_content <- read_lines(.x)
    test_lines <- grep("^Best models for iteration 1:  ", file_content)
    start_line <- test_lines + which(file_content[test_lines:length(file_content)] == "| Model | Count |")[1] - 1
    end_line <- grep("^### Model update  ", file_content)[1] - 1
    table_content <- file_content[start_line:end_line]
    table <- markdown_table_to_tibble(table_content)
    table$test <- gsub("\\_log.md$", "", basename(.x))
    table <- table %>% rename(model = Count, count = Model)
    return(table)
  })
  initial_model_table <- initial_model_tables %>% bind_rows()
  return(initial_model_table)
}

# Function to plot BIC of trained models
plot_BIC_trained_models <- function(concat_test_sum, output_folder) {
  plot_BIC_trained_model <- concat_test_sum %>%
    group_by(test) %>%
    filter(model_type == "trained" & F_type == "FO") %>%
    ungroup() %>%
    ggplot(aes(x = max_tree_size, y = BIC)) +
    geom_line() +
    theme_light() +
    labs(title = "BIC of trained models on concatenated testing loci", x = "Maximum subtree size", y = "BIC")
  ggsave(file.path(output_folder, "BIC_trained_model.png"), plot_BIC_trained_model, width = 8, height = 6)
}

# Function to plot BIC of all models
plot_BIC_all_models <- function(concat_test_sum, output_folder) {
  trained_models_test <- concat_test_sum %>%
    filter(model_type == "trained") %>%
    mutate(model_string = str_c(model_type, "_", F_type))
  other_models_test <- concat_test_sum %>%
    filter(model_type == "existed") %>%
    group_by(model) %>%
    filter(n() > 3) %>%
    ungroup()

  plot_all_models <- rbind(trained_models_test, other_models_test)

  model_order <- plot_all_models %>%
    group_by(model_string) %>%
    summarise(min_BIC = min(BIC, na.rm = TRUE)) %>%
    arrange(min_BIC) %>%
    pull(model_string)

  plot_all_models <- plot_all_models %>%
    mutate(model_string = factor(model_string, levels = model_order))

  plot_BIC_all_models <- plot_all_models %>%
    ggplot(aes(x = max_tree_size, y = BIC)) +
    geom_line() +
    facet_wrap(~model_string, scales = "free_y", ncol = 4) +
    theme_light() +
    labs(title = "BIC of all models on concatenated testing loci", x = "Maximum subtree size", y = "BIC")

  ggsave(file.path(output_folder, "BIC_all_models.png"), plot_BIC_all_models, width = 10, height = 8)
}

# Function to plot initial model distribution
plot_initial_model_distribution <- function(initial_model_table, output_folder) {
  plot_initial_model_distribution <- initial_model_table %>%
    mutate(count_ratio = count / sum(count)) %>%
    mutate(max_tree_size = str_extract(test, "\\d+")) %>%
    mutate(max_tree_size = as.numeric(max_tree_size)) %>%
    ggplot(aes(x = max_tree_size, y = count_ratio, group = model, color = model)) +
    geom_line() +
    theme_light() +
    labs(title = "Initial model distribution on different maximum subtree size", x = "Maximum subtree size", y = "Count ratio")

  ggsave(file.path(output_folder, "initial_model_distribution.png"), plot_initial_model_distribution, width = 8, height = 6)
}

# Main function to run the analysis
run_tree_size_analysis <- function(logfile_folder) {
  log_list <- dir(logfile_folder, full.names = TRUE)
  output_folder <- dirname(logfile_folder)

  concat_test_sum <- process_concat_test_tables(log_list)
  write.csv(concat_test_sum, file.path(output_folder, "concat_test_sum.csv"), row.names = FALSE)

  initial_model_table <- process_initial_model_tables(log_list)
  write.csv(initial_model_table, file.path(output_folder, "initial_model_sum.csv"), row.names = FALSE)

  plot_BIC_trained_models(concat_test_sum, output_folder)
  plot_BIC_all_models(concat_test_sum, output_folder)
  plot_initial_model_distribution(initial_model_table, output_folder)
}

# Parse command line arguments
args <- commandArgs(trailingOnly = TRUE)

if (length(args) == 0) {
  stop("No logfile_folder provided. Usage: Rscript summary_tree_size.R <logfile_folder>")
}

run_tree_size_analysis(args[1])
