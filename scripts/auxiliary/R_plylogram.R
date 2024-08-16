#!/usr/bin/env Rscript

# Load required libraries
library(ggplot2)
library(ggtree)

# Plot trees side-by-side using ggtree
phylograms <- function(tree, y_scale = -5, subtitle = "", node_label = NULL) {
  # Determine the color scale based on the node_label parameter
  color_name <- NULL
  color_limits <- NULL

  if (node_label == "PP") {
    color_name <- "Posterior Probability"
    color_limits <- c(0, 1)
  } else if (node_label == "BS") {
    color_name <- "Bootstrap Support"
    color_limits <- c(0, 100)
  } else {
    color_name <- NULL
  }

  # Plot the tree
  if (is.null(color_name)) {
    plot <- ggtree(tree, cex = 0.8, lwd = 0.5)
  } else {
  plot <- ggtree(tree, cex = 0.8, lwd = 0.5,aes(color = ifelse(is.na(as.numeric(label)), 0, as.numeric(label)))) +
    scale_color_continuous(
      high = "black", low = "red",
      name = color_name, limits = color_limits,
      guide = if (!is.null(color_name)) guide_colourbar(barwidth = 10) else NULL
    ) 
  }
  plot <- plot +
    geom_treescale(y = y_scale - 20, color = "black", fontsize = 5) +
    labs(subtitle = subtitle) +
    theme(legend.position = if (!is.null(color_name)) "bottom" else "none")

  return(plot)
}

