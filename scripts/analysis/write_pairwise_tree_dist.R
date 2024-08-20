library(ape)
library(phangorn)
library(ggplot2)
library(dplyr)
library(tidyr)
library(tibble)
library(vegan)
library(ggrepel)
library(dendextend)

# Function to extract tree name from file path
extract_tree_name <- function(file_path) {
  # Extract file name without extension
  basename(file_path) %>% tools::file_path_sans_ext()
}

# Source auxiliary functions
source("./auxiliary/R_tree_tool.R")
source("./auxiliary/R_extended_plots.R")
source("./auxiliary/R_ggplot_plot.R")

# --- Main script ---

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 1) {
  stop("Usage: Rscript script.R <dir_path>")
}

# Assign command line argument to variable
dir_path <- args[1]

# Get all tree files in the directory
tree_files <- list.files(dir_path, pattern = "\\..*tre.*$", ignore.case = TRUE)

# If only have one tree file, exit
if (length(tree_files) < 2) {
  stop("At least two tree files are required for pairwise comparison.")
}

# Read all trees into a list
trees <- lapply(tree_files, function(x) read.tree(file.path(dir_path, x)))
names(trees) <- extract_tree_name(tree_files)

# Generate all pairwise combinations of trees
tree_combinations <- combn(names(trees), 2, simplify = FALSE)

# Calculate distances for all pairs of tree files
distance_results <- lapply(tree_combinations, function(pair) {
  tree1_name <- pair[1]
  tree2_name <- pair[2]
  tree1 <- trees[[tree1_name]]
  tree2 <- trees[[tree2_name]]
  
  distances <- calculate_tree_distances(tree1, tree2)
  distances$Tree1 <- tree1_name
  distances$Tree2 <- tree2_name
  distances
})

# Combine distance results into a single data frame
all_distances <- bind_rows(distance_results)

# Save distance results to CSV file
write.csv(all_distances, file = file.path(dir_path, "tree_pairwise_compare.csv"), row.names = FALSE)

# Prepare data for heatmap and NMDS
distance_matrix_nRF <- all_distances %>%
  select(Tree1, Tree2, nRF) %>%
  pivot_wider(names_from = Tree2, values_from = nRF) %>%
  column_to_rownames(var = "Tree1") %>%
  as.matrix()

distance_matrix_nRF[is.na(distance_matrix_nRF)] <- 0

# Generate and save heatmap
heatmap_RF <- treedist_heatmap(all_distances, "RF_dist")
save_heatmap(heatmap_RF, file.path(dir_path, "RF_heatmap.png"))
heatmap_nRF <- treedist_heatmap(all_distances, "nRF")
save_heatmap(heatmap_nRF, file.path(dir_path, "nRF_heatmap.png"))

# Generate and save NMDS plot
nmds_plot <- plot_NMDS(distance_matrix_nRF)
save_NMDS_plot(nmds_plot, file.path(dir_path, "nRF_NMDS.png"))