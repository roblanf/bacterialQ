#' Generates a heatmap with hierarchical clustering from a distance matrix.
#' @param distance_table A tibble or data frame representing the distance matrix. The distance matrix should have row labels in one column 
#' and the corresponding distances in the other columns.
#' @param value_col A string specifying the name of the column in `distance_table` that contains the values to be displayed in the heatmap.
#' @param row_label_col A string specifying the name of the column in `distance_table` that contains the row labels.
#' @param col_label_col A string specifying the name of the columns in `distance_table` that contains the column labels.
#' @return A ggplot object representing the heatmap with hierarchical clustering.

label_clustered_heatmap <- function(distance_table, value_col, row_label_col, col_label_col) {
  library(ggplot2)
  library(dplyr)
  library(tidyr)

  # Perform hierarchical clustering on the rows and columns
  hc_rows <- hclust(as.dist(distance_table %>% select(-all_of(row_label_col))), method = "complete")
  hc_cols <- hclust(as.dist(t(distance_table %>% select(-all_of(col_label_col)))), method = "complete")

  # Convert the distance matrix to long format
  melted_matrix <- distance_table %>%
    as.data.frame() %>%
    pivot_longer(cols = -all_of(row_label_col), names_to = col_label_col, values_to = value_col) %>%
    mutate(
      !!sym(row_label_col) := factor(!!sym(row_label_col), levels = hc_rows$labels[hc_rows$order]),
      !!sym(col_label_col) := factor(!!sym(col_label_col), levels = hc_cols$labels[hc_cols$order])
    )

  # Generate the heatmap
  heatmap <- ggplot(melted_matrix, aes_string(x = col_label_col, y = row_label_col, fill = value_col)) +
    geom_tile() +
    geom_text(aes_string(label = value_col), size = 3) +
    coord_equal() +
    scale_fill_gradient(low = "white", high = "red") +
    labs(x = col_label_col, y = row_label_col, fill = value_col) +
    theme_light() +
    theme(
      axis.text = element_text(size = 10),
      panel.background = element_rect(fill = "white"),
      panel.grid = element_blank(),
      axis.text.x = element_text(angle = 45, hjust = 1)
    )

  return(heatmap)
}

#' Generates a heatmap from a tree distance matrix with hierarchical clustering.

#' @param distance_table A tibble or data frame representing the tree distance matrix. The distance matrix should have row labels in the 
#' `Tree1` column and corresponding distances in the `Tree2` column.
#' @param value_col A string specifying the name of the column in `distance_table` that contains the values to be displayed in the heatmap.
#' @return A ggplot object representing the heatmap with hierarchical clustering.
treedist_heatmap <- function(distance_table, value_col) {
  # Here, 'Tree1' and 'Tree2' are assumed to be the row and column labels in the distance matrix
  label_clustered_heatmap(distance_table, value_col, row_label_col = "Tree1", col_label_col = "Tree2")
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