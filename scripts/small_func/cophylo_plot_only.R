#!/usr/bin/env Rscript

# Load required libraries
library(ape)
library(phangorn)
library(ggplot2)
library(ggtree)
library(phytools)

source("../auxilliray/R_cophylo_plot.R")
source("../auxilliray/R_tree_tool.R")
source("../auxilliray/R_plylogram.R")

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)
tree1_path <- args[1]
tree2_path <- args[2]
output_dir <- args[3]

# Read the tree files
tree1 <- read.tree(tree1_path)
tree2 <- read.tree(tree2_path)

# Find common taxa
common_taxa <- intersect(tree1$tip.label, tree2$tip.label)

# Subset trees to common taxa
tree1 <- drop.tip(tree1, setdiff(tree1$tip.label, common_taxa))
tree2 <- drop.tip(tree2, setdiff(tree2$tip.label, common_taxa))

# Define a function to extract the tree name from the file path
extract_tree_name <- function(file_path) {
  # Remove the directory path and file extension from the file path
  tree_name <- sub("^.*\\/", "", file_path)
  tree_name <- sub("\\..*$", "", tree_name)
  return(tree_name)
}

# Extract tree names from file paths
tree1_name <- extract_tree_name(tree1_path)
tree2_name <- extract_tree_name(tree2_path)

# Process node labels
tree1 <- process_node_labels(tree1)
tree2 <- process_node_labels(tree2)

p1 <- phylograms(tree1, subtitle = "Tree 1")
p2 <- phylograms(tree2, subtitle = "Tree 2")

ggsave(filename = paste0(output_dir, "/", tree1_name, "_", tree2_name, "_ggtree.pdf"), plot = gridExtra::grid.arrange(p1, p2, ncol = 2), width = 14, height = 22)


# Calculate normalized Robinson-Foulds distance
nRF_dist <- RF.dist(tree1, tree2, normalize = TRUE, check.labels = TRUE)

if (nRF_dist >= 0.05) {
  # Generate cophylo plot
  generate_cophylo_plot(tree1, tree2, paste0(output_dir, "/", tree1_name, "_", tree2_name, "_cophylo.pdf"))
  cat("Cophylo plot generated successfully.\n")
  cat("![Cophylo plot](cophylo_plot.png)")
} else {
  cat("The normalized Robinson-Foulds distance is less than 1, cophylo plot will not be shown.")
}