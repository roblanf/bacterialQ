#!/usr/bin/env Rscript

# Load required libraries
library(ggplot2)
library(ggtree)

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

