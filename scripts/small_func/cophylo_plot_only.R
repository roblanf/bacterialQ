#!/usr/bin/env Rscript

# Load required libraries
library(ape)
library(phangorn)
library(ggplot2)
library(ggtree)
library(phytools)

source("../auxiliary/R_cophylo_plot.R")
source("../auxiliary/R_tree_tool.R")
source("../auxiliary/R_plylogram.R")

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)
tree1_path <- args[1]
tree2_path <- args[2]
output_dir <- args[3]

# Read the tree files
tree1_raw <- read.tree(tree1_path)
tree2_raw <- read.tree(tree2_path)

# Make sure tree1 and tree2 shares the same taxa
standard_trees <- standardize_trees(tree1_raw, tree2_raw)
tree1 <- standard_trees[[1]]
tree2 <- standard_trees[[2]]

# Determine weather two trees are rooted or not
ifroot <- is.rooted(tree1) && is.rooted(tree1)

# Make sure the style of node label is consistent
same_label_trees <- keep_same_tree_label(tree1, tree2)
tree1 <- same_label_trees[[1]]
tree2 <- same_label_trees[[2]]
nodel_label_type <- same_label_trees[[3]]

# Define a function to extract the tree name from the file path
extract_tree_name <- function(file_path) {
  # Remove the directory path and file extension from the file path
  tree_name <- sub("^.*\\/", "", file_path)
  tree_name <- sub("\\.[^.]*$", "", tree_name)
  return(tree_name)
}

# Extract tree names from file paths
tree1_name <- extract_tree_name(tree1_path)
tree2_name <- extract_tree_name(tree2_path)

p1 <- phylograms(tree1, subtitle = "Tree 1")
p2 <- phylograms(tree2, subtitle = "Tree 2")

ggsave(filename = paste0(output_dir, "/", tree1_name, "_", tree2_name, "_ggtree.pdf"), plot = gridExtra::grid.arrange(p1, p2, ncol = 2), width = 14, height = 22)


# Calculate normalized Robinson-Foulds distance
nRF_dist <- RF.dist(tree1, tree2, normalize = TRUE, check.labels = TRUE)

if (nRF_dist >= 0.05 && length(tree1$tip.label) <= 5000) {
  # Generate cophylo plot
  generate_cophylo_plot(tree1, tree2, paste0(output_dir, "/", tree1_name, "_", tree2_name, "_cophylo.pdf"), nodel_label_type)
  cat("Cophylo plot generated successfully.\n")
  cat("![Cophylo plot](cophylo_plot.pdf)")
} else {
  if (length(tree1$tip.label) > 5000) {
    cat("The number of taxa is too large, please plot it manully.")
  }
  if (result_df$nRF < 0.1) {
  cat("The normalized Robinson-Foulds distance is less than 0.1, cophylo plot will not be shown.")
  }
}