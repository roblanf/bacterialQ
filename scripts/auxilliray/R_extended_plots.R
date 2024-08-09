# Function to generate heatmap from distance matrix
#' @description Generates a heatmap from a distance matrix with hierarchical clustering.
#' @param distance_table A tibble which should be formatted as cols: Tree1, Tree2, value1, value2, ...
#' @param value_col Column name in distance_table for heatmap values
generate_heatmap <- function(distance_table, value_col) {
  library(ggplot2)
  library(dplyr)
  library(tidyr)

  # Perform hierarchical clustering
  hc <- hclust(as.dist(distance_table), method = "complete")

  # Convert distance matrix to long format using pivot_longer
  melted_matrix <- distance_table %>%
    as.data.frame() %>%
    tibble::rownames_to_column("Tree1") %>%
    pivot_longer(cols = -Tree1, names_to = "Tree2", values_to = "value") %>%
    mutate(
      Tree1 = factor(Tree1, levels = hc$labels[hc$order]),
      Tree2 = factor(Tree2, levels = hc$labels[hc$order])
    ) %>%
    filter(as.numeric(Tree1) >= as.numeric(Tree2)) # Filter for lower triangle

  # Generate heatmap
  heatmap <- ggplot(melted_matrix, aes(x = Tree1, y = Tree2, fill = value)) +
    geom_tile() +
    geom_text(aes(label = value), size = 3) +
    coord_equal() +
    scale_fill_gradient(low = "white", high = "red") +
    labs(x = "Tree 1", y = "Tree 2", fill = value_col) +
    theme_light() +
    theme(
      axis.text = element_text(size = 10),
      panel.background = element_rect(fill = "white"),
      panel.grid = element_blank(),
      axis.text.x = element_text(angle = 45, hjust = 1)
    )

  return(heatmap)
}

save_heatmap <- function(heatmap, output_path) {
  num_x_labels <- length(heatmap$data$Tree1)
  fig_size <- max(6, num_x_labels / 1.5)
  ggsave(output_path, heatmap, width = fig_size, height = fig_size)
}

# Function to generate NMDS plots with point shape customization
#' @description Generates a Non-metric Multidimensional Scaling (NMDS) plot 
#'              from a distance matrix, with customizable point shapes.
#' @param distance_matrix A distance matrix
#' @param point_shape Shape of the points (default: 21, filled circle). 
#'                   See ?pch for more options.
plot_NMDS <- function(distance_matrix, point_shape = 21) {
  library(ggplot2)
  library(vegan)
  library(ggrepel)
  
  # Check the rank of the matrix
  matrix_rank <- qr(distance_matrix)$rank
  if (matrix_rank <= 2) {
    warning("Matrix rank is less than 3. NMDS computation cannot proceed.")
    return(NULL)
  }

  # Perform NMDS
  nmds_result <- metaMDS(
    comm = distance_matrix,
    autotransform = FALSE,
    distance = "euclidean",
    engine = "monoMDS",
    k = 2,
    weakties = TRUE,
    model = "global",
    maxit = 300,
    try = 50,
    trymax = 100
  )

  # Prepare data for plot
  nmds_points <- data.frame(nmds_result$points)

  # Create the plot with customizable point shape
  p <- ggplot(data = nmds_points, aes(x = MDS1, y = MDS2, label = rownames(distance_matrix))) +
    geom_point(shape = point_shape, size = 3, fill = "blue") +  # Customizable point shape and fill
    coord_equal() +
    theme_bw() +
    theme(
      axis.text = element_blank()
    ) +
    geom_text_repel(max.overlaps = Inf, size = 3)

  return(p)
}

save_NMDS_plot <- function(plot, output_path) {
  ggsave(filename = output_path, plot = plot)
}