library(phytools)

generate_cophylo_plot <- function(rooted_tree1, rooted_tree2, output_path, node_label = "null") {
  # Create cophylo object
  obj <- cophylo(rooted_tree1, rooted_tree2)
  
  # Calculate figure dimensions
  Nspecies <- length(rooted_tree1$tip.label)
  if (Nspecies < 300) {
    fig_length <- 5 + Nspecies %/% 20
    fig_width <- 6 + Nspecies %/% 50
  } else {
    fig_length <- 10 + Nspecies %/% 30
    fig_width <- 9 + Nspecies %/% 100
  }

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

    if (node_label == "PP") {
      bs <- sapply(tree$edge[, 2] - Ntip(tree),
        function(x, y) {
          if (x >= 2) {
            value <- as.numeric(y[x])
            return(value)
          } else {
            return("")
          }
        },
        y = node_labels
      )
    } else if (node_label == "BS") {
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
    } else {
      bs <- rep("", length(tree$edge[, 2]))
    }
    
    edgelabels.cophylo(bs, frame = "none", cex = 0.5, adj = c(0.4, -0.2), which = position)
  }

  # Function to create a color gradient based on node_label
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

    if (node_label == "PP") {
      color_limits <- c(0, 1)
    } else if (node_label == "BS") {
      color_limits <- c(0, 100)
    } else {
      return(rep("black", length(support_values))) # No color if node_label is NULL
    }

    # Create color gradient from red to black
    create_rgb_color <- function(value, limits) {
      if (is.na(value)) {
        return(rgb(0, 0, 0, maxColorValue = 255))
      }
      normalized <- (value - limits[1]) / diff(limits)
      red <- 255
      green <- 0
      blue <- 0
      # Interpolate from red to black
      red <- red * (1 - normalized)
      green <- green * (1 - normalized)
      blue <- blue * (1 - normalized)
      return(rgb(red, green, blue, maxColorValue = 255))
    }

    edge_colors <- sapply(support_values, create_rgb_color, limits = color_limits)

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


generate_cophylo_plot2 <- function(rooted_tree1, rooted_tree2, output_path, label_types = c("null", "null"), assoc = NULL, plot_type = "phylogram") {
  # Create cophylo object
    if (!is.null(assoc)) {
    cat("Plotted with defined association.\n")
  obj <- cophylo(rooted_tree1, rooted_tree2, assoc = assoc, rotate = TRUE)
    } else {
    cat("Plotted with precise name matching.\n")
  obj <- cophylo(rooted_tree1, rooted_tree2, rotate = TRUE)
    }

  # Calculate figure dimensions
  Nspecies <- length(rooted_tree1$tip.label)
  if (Nspecies < 300) {
    fig_length <- 2 + Nspecies %/% 15
    fig_width <- 4 + Nspecies %/% 40
  } else {
    fig_length <- 10 + Nspecies %/% 30
    fig_width <- 13 + Nspecies %/% 100
  }

  # Open pdf device with reduced resolution
  pdf(output_path, width = fig_width, height = fig_length, pointsize = 8)

  # Function to process bootstrap proportions and add edge labels
  add_edge_labels <- function(tree, position, label_type) {
    node_labels <- tree$node.label

    if (label_type == "PP") {
      bs <- sapply(tree$edge[, 2] - Ntip(tree),
        function(x, y) {
          if (x >= 2) {
            value <- as.numeric(y[x])
            return(value)
          } else {
            return("")
          }
        },
        y = node_labels
      )
    } else if (label_type == "BS") {
      bs <- sapply(tree$edge[, 2] - Ntip(tree),
        function(x, y) {
          if (x >= 2) {
            value <- as.numeric(y[x])
          } else {
            return("")
          }
        },
        y = node_labels
      )
    } else {
      bs <- rep("", length(tree$edge[, 2]))
    }
    
    edgelabels.cophylo(bs, frame = "none", cex = 0.4, adj = c(0.4, -0.2), which = position)
  }

  # Function to create a color gradient based on node_label
  create_edge_colors <- function(tree, label_type) {
    node_labels <- tree$node.label
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

    if (label_type == "PP") {
      color_limits <- c(0, 1)
    } else if (label_type == "BS") {
      color_limits <- c(0, 100)
    } else {
      return(rep("black", length(support_values))) # No color if label_type is NULL
    }

    # Create color gradient from red to black
    create_rgb_color <- function(value, limits) {
      if (is.na(value)) {
        return(rgb(0, 0, 0, maxColorValue = 255))
      }
      normalized <- (value - limits[1]) / diff(limits)
      red <- 255
      green <- 0
      blue <- 0
      # Interpolate from red to black
      red <- red * (1 - normalized)
      green <- green * (1 - normalized)
      blue <- blue * (1 - normalized)
      return(rgb(red, green, blue, maxColorValue = 255))
    }

    edge_colors <- sapply(support_values, create_rgb_color, limits = color_limits)

    return(edge_colors)
  }

  # Create edge colors for both trees
  edge_colors <- list(
    left = create_edge_colors(obj$trees[[1]], label_type = label_types[[1]]),
    right = create_edge_colors(obj$trees[[2]], label_type = label_types[[2]])
  )

    plot(obj, type = c(plot_type, plot_type), link.type="curved", link.lwd =1.5, fsize = 0.4,
       link.lty="solid", link.col=make.transparent("red", 0.25), use.edge.length = TRUE, edge.col = edge_colors)

  # Apply the function to both trees
  add_edge_labels(obj$trees[[1]], "left", label_type = label_types[[1]])
  add_edge_labels(obj$trees[[2]], "right", label_type = label_types[[2]])

  # Close PDF device
  dev.off()
}
