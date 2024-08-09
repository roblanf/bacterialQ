#!/usr/bin/env Rscript

# Load required libraries
library(ape)
library(phangorn)
library(ggplot2)
library(ggtree)
library(phytools)

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

process_node_labels <- function(tree) {
  #' @description
  #' Process the node labels of a tree. Convert labels to numeric, scale if mean is less than 1, and convert back to character.
  #' @param tree A tree object read by the ape package.
  #' @return A tree object with processed node labels.

  # Convert node labels to numeric
  node_labels <- as.numeric(tree$node.label)

  # Check if the mean of numeric labels is less than 1
  if (mean(node_labels, na.rm = TRUE) < 1) {
    # Scale the labels by 100 and convert to integer
    node_labels <- as.integer(node_labels * 100)
  }

  # Convert back to character and replace the original labels
  tree$node.label <- as.character(node_labels)

  return(tree)
}

tree1 <- process_node_labels(tree1)
tree2 <- process_node_labels(tree2)

# Plot trees side-by-side using ggtree
phylograms <- function(tree, y_scale = -5, subtitle = "") {
  ggtree(tree, cex = 0.8, lwd = 0.5, aes(color = ifelse(is.na(as.numeric(label)), 100, as.numeric(label)))) +
    scale_color_continuous(
      high = "black", low = "red",
      name = "Posterior Probability", limits = c(0, 100),
      guide = guide_colourbar(barwidth = 10)
    ) +
    geom_treescale(y = y_scale - 20, color = "black", fontsize = 5) +
    labs(subtitle = subtitle) +
    theme(legend.position = "bottom")
}

p1 <- phylograms(tree1, subtitle = "Tree 1")
p2 <- phylograms(tree2, subtitle = "Tree 2")

ggsave(filename = paste0(output_dir, "/", tree1_name, "_", tree2_name, "_ggtree.pdf"), plot = gridExtra::grid.arrange(p1, p2, ncol = 2), width = 14, height = 22)


# Calculate normalized Robinson-Foulds distance
nRF_dist <- RF.dist(tree1, tree2, normalize = TRUE, check.labels = TRUE)

generate_cophylo_plot <- function(rooted_tree1, rooted_tree2, output_path) {
  # Create cophylo object
  obj <- cophylo(rooted_tree1, rooted_tree2)

  # Calculate figure dimensions
  Nspecies <- length(rooted_tree1$tip.label)
  fig_length <- Nspecies %/% 50
  fig_width <- 12 + Nspecies %/% 100

  # Open pdf device with reduced resolution
  pdf(output_path, width = fig_width, height = fig_length, pointsize = 8)

  # Function to determine if node labels should be multiplied by 100
  should_multiply_by_100 <- function(labels) {
    numeric_labels <- as.numeric(labels)
    # Check if more than half of the labels are less than 1
    return(mean(numeric_labels < 1, na.rm = TRUE) > 0.5)
  }

  # Function to process bootstrap proportions and add edge labels
  add_edge_labels <- function(tree, position) {
    node_labels <- tree$node.label
    multiply_by_100 <- should_multiply_by_100(node_labels)

    bs <- sapply(tree$edge[, 2] - Ntip(tree),
      function(x, y) {
        if (x >= 2) {
          value <- as.numeric(y[x])
          if (multiply_by_100) {
            return(value * 100)
          } else {
            return(value)
          }
        } else {
          return("")
        }
      },
      y = node_labels
    )

    edgelabels.cophylo(bs, frame = "none", cex = 0.5, adj = c(0.4, -0.2), which = position)
  }

  # Function to create a color gradient based on Posterior Probabilitys
  create_edge_colors <- function(tree) {
    node_labels <- as.numeric(tree$node.label)
    support_values <- sapply(tree$edge[, 2] - Ntip(tree),
      function(x, y) {
        if (x >= 2) {
          return(as.numeric(y[x]))
        } else {
          return(NA)
        }
      },
      y = node_labels
    )

    # Create color gradient from red to black
    create_rgb_color <- function(value) {
      if (is.na(value)) {
        return(rgb(0, 0, 0, maxColorValue = 255))
      }
      red <- 255
      green <- 0
      blue <- 0
      # Interpolate from red to black
      red <- red * (1 - value)
      green <- green * (1 - value)
      blue <- blue * (1 - value)
      return(rgb(red, green, blue, maxColorValue = 255))
    }

    edge_colors <- sapply(support_values / 100, create_rgb_color)

    return(edge_colors)
  }

  # Create edge colors for both trees
  edge_colors <- list(
    left = create_edge_colors(obj$trees[[1]]),
    right = create_edge_colors(obj$trees[[2]])
  )

  # Plot cophylo with edge colors and without node or edge labels
  plot(obj, type = c("phylogram", "phylogram"), fsize = 0.3, part = 0.45, show.tip.label = FALSE, link.type = "curved", use.edge.length = TRUE, edge.col = edge_colors)

  # Apply the function to both trees
  add_edge_labels(obj$trees[[1]], "left")
  add_edge_labels(obj$trees[[2]], "right")

  # Close PDF device
  dev.off()
}

if (nRF_dist >= 0.05) {
  # Generate cophylo plot
  generate_cophylo_plot(tree1, tree2, paste0(output_dir, "/", tree1_name, "_", tree2_name, "_cophylo.pdf"))
  cat("Cophylo plot generated successfully.\n")
  cat("![Cophylo plot](cophylo_plot.png)")
} else {
  cat("The normalized Robinson-Foulds distance is less than 1, cophylo plot will not be shown.")
}