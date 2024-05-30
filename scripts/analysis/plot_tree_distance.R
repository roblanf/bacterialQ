# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(stringr)
library(vegan)
library(ggrepel)

# Define functions
read_and_process_summary <- function(summary_path) {
  # Read the summary file
  summary_df <- read.csv(summary_path)

  # Abbreviate the Tree1 and Tree2 values
  summary_df$Tree1 <- str_replace(summary_df$Tree1, ".*_(\\d+_\\d+)$", "\\1")
  summary_df$Tree2 <- str_replace(summary_df$Tree2, ".*_(\\d+_\\d+)$", "\\1")

  # Convert Tree1 and Tree2 to numeric for ordering
  summary_df$Tree1_num <- as.numeric(str_extract(summary_df$Tree1, "\\d+"))
  summary_df$Tree2_num <- as.numeric(str_extract(summary_df$Tree2, "\\d+"))
  summary_df <- summary_df %>% replace_na(list(Tree1_num = 10000, Tree2_num = 10000))

  summary_df2 <- summary_df %>%
    rename(Tree1 = Tree2, Tree2 = Tree1, Tree1_num = Tree2_num, Tree2_num = Tree1_num)

  summary_df <- rbind(summary_df, summary_df2)
  return(summary_df)
}

plot_heatmap <- function(summary_df, output_path, suffix) {
  # Filter the data to only include lower triangle values
  summary_df$Tree1_loop <- as.numeric(str_extract(summary_df$Tree1, "\\d+$"))
  summary_df$Tree2_loop <- as.numeric(str_extract(summary_df$Tree2, "\\d+$"))
  summary_df <- summary_df %>% filter(Tree1_num <= Tree2_num) %>% filter(!(Tree1_num == Tree2_num & Tree1_loop > Tree2_loop))
  # Plot the heatmap
  p <- ggplot(summary_df, aes(x = reorder(Tree1, Tree1_num), y = reorder(Tree2, Tree2_num), fill = RF_dist)) +
    geom_tile() +
    geom_text(aes(label = round(RF_dist, 2)), size = 3, color = "black") +  # Add text to each cell
    coord_equal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    scale_fill_gradient(low = "white", high = "red") +
    labs(x = "Tree1", y = "Tree2", fill = "RF_dist") +
    theme_light() +
    theme(axis.text = element_text(size = 10),
          panel.background = element_rect(fill = "white"),
          panel.grid.major = element_blank(),  # Remove major grid lines
          panel.grid.minor = element_blank())  # Remove minor grid lines

  # Save the plot
  ggsave(filename = paste0(output_path, "/RF_dist_heatmap_", suffix, ".png"), plot = p)
}

plot_NMDS <- function(summary_df, output_path, suffix) {
  # Prepare data for NMDS
  nRF_matrix <- summary_df %>% select(Tree1, Tree2, nRF) %>% spread(Tree2, nRF)
  namerow <- nRF_matrix %>% pull(Tree1)
  nRF_matrix <- nRF_matrix %>% select(-Tree1) %>% as.matrix()
  rownames(nRF_matrix) <- namerow
  print(nRF_matrix)
  
  # Perform NMDS
  z <- metaMDS(comm = nRF_matrix,
               autotransform = FALSE,
               distance = "euclidean",
               engine = "monoMDS",
               k = 2,
               weakties = TRUE,
               model = "global",
               maxit = 300,
               try = 50,
               trymax = 100)

  # Prepare data for plot
  z.points <- data.frame(z$points)

  # Create the plot
  p <- ggplot(data = z.points, aes(x = MDS1, y = MDS2, label = rownames(nRF_matrix))) +
    geom_point() +
    coord_equal() +
    theme_bw() + 
    theme(axis.text.x = element_blank(),  # remove x-axis text
          axis.text.y = element_blank()) +  # remove y-axis text
    geom_text_repel()

  # Save the plot
  ggsave(filename = paste0(output_path, "/nRF_dist_NMDS_", suffix, ".png"), plot = p)
}

# Main script
main <- function(summary_path) {
  # Get the directory path from the summary path
  dir_path <- dirname(summary_path)

  # Read and process the summary file
  summary_df <- read_and_process_summary(summary_path)

  # Plot and save the heatmap and NMDS for the raw data
  plot_heatmap(summary_df, dir_path, "raw")
  plot_NMDS(summary_df, dir_path, "raw")

  # Exclude the rows where Tree1 or Tree2 is the reference tree
  summary_df_no_ref <- summary_df %>% filter(Tree1 != "ref_tree" & Tree2 != "ref_tree")

  # Plot and save the heatmap and NMDS for the data without the reference tree
  plot_heatmap(summary_df_no_ref, dir_path, "no_ref")
  plot_NMDS(summary_df_no_ref, dir_path, "no_ref")
}

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 1) {
  stop("Usage: Rscript script.R <tree_summary.csv>")
}

main(args[1])