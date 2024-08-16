#' Generates a heatmap with hierarchical clustering from a distance matrix.
#' @param distance_table A tibble or data frame representing the distance matrix. The distance matrix should have row labels in one column 
#' and the corresponding distances in the other columns.
#' @param value_col A string specifying the name of the column in `distance_table` that contains the values to be displayed in the heatmap.
#' @param row_label_col A string specifying the name of the column in `distance_table` that contains the row labels.
#' @param col_label_col A string specifying the name of the columns in `distance_table` that contains the column labels.
#' @return A ggplot object representing the heatmap with hierarchical clustering.

label_clustered_heatmap <- function(distance_df, value_col, cluster_col1, cluster_col2) {
  library(ggplot2)
  library(dplyr)
  library(tidyr)

# Create a symmetric dataframe
  distance_df_sym <- distance_df %>%
    rename(!!sym(cluster_col1) := !!sym(cluster_col2), !!sym(cluster_col2) := !!sym(cluster_col1))
  distance_df <- rbind(distance_df, distance_df_sym)
  
  # Create the distance matrix
  dist_matrix <- distance_df %>%
    select(!!sym(cluster_col1), !!sym(cluster_col2), !!sym(value_col)) %>%
    spread(!!sym(cluster_col2), !!sym(value_col)) %>%
    column_to_rownames(var = cluster_col1) %>%
    as.matrix()
  
  dist_matrix[is.na(dist_matrix)] <- 0  # Replace NA values with 0
  
  # Perform hierarchical clustering
  hc <- hclust(as.dist(dist_matrix), method = "complete")
  
  # Create a dendrogram
  dend <- as.dendrogram(hc)
  
  # Generate heatmap with clustering
  distance_df <- distance_df %>%
    mutate(!!sym(cluster_col1) := factor(!!sym(cluster_col1), levels = hc$labels[hc$order]),
           !!sym(cluster_col2) := factor(!!sym(cluster_col2), levels = hc$labels[hc$order]))
  
  # Filter to only lower triangle
  distance_df <- distance_df %>%
    filter(as.numeric(!!sym(cluster_col1)) >= as.numeric(!!sym(cluster_col2)))
  
  # Generate heatmap
  heatmap <- ggplot(distance_df, aes_string(x = cluster_col1, y = cluster_col2, fill = value_col)) +
    geom_tile() +
    geom_text(aes_string(label = value_col), size = 3) +  # Add text annotations
    coord_equal() +
    scale_fill_gradient(low = "white", high = "red") +
    labs(x = cluster_col1, y = cluster_col2, fill = value_col) +
    theme_light() +
    theme(
      axis.text = element_text(size = 10),
      panel.background = element_rect(fill = "white"),
      panel.grid.major = element_blank(), # Remove major grid lines
      panel.grid.minor = element_blank(),
      axis.text.x = element_text(angle = 45, hjust = 1)
    ) +
    scale_x_discrete(limits = hc$labels[hc$order]) +  # Reorder x-axis
    scale_y_discrete(limits = hc$labels[hc$order])    # Reorder y-axis
  return(heatmap)
}
#' Generates a heatmap from a tree distance matrix with hierarchical clustering.

#' @param distance_table A tibble or data frame representing the tree distance matrix. The distance matrix should have row labels in the 
#' `Tree1` column and corresponding distances in the `Tree2` column.
#' @param value_col A string specifying the name of the column in `distance_table` that contains the values to be displayed in the heatmap.
#' @return A ggplot object representing the heatmap with hierarchical clustering.
treedist_heatmap <- function(distance_table, value_col) {
  # Here, 'Tree1' and 'Tree2' are assumed to be the row and column labels in the distance matrix
  label_clustered_heatmap(distance_table, value_col, cluster_col1 = "Tree1", cluster_col2 = "Tree2")
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