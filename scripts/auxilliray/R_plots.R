library(tidyverse)

#' @description Generate a lower triangle heatmap from a symmetric x_col and y_col data frame.
#' @param data Data frame containing the data
#' @param x_col Column name for the x-axis
#' @param y_col Column name for the y-axis
#' @param fill_col Column name for the fill values
#' @param min_val Minimum value for the fill scale
#' @param max_val Maximum value for the fill scale
#' @param significant_val Value above which a star should be displayed
#' @param type Type of the heatmap, either "cor" for correlation or "dist" for distance
#' @return A ggplot object representing the heatmap
generate_lower_triangle_heatmap <- function(data, x_col, y_col, fill_col, min_val, max_val, significant_val, type = "cor") {
  # Convert columns to numeric if they are factors
  if (is.factor(data[[x_col]]) && is.factor(data[[y_col]])) {
    x_levels <- levels(data[[x_col]])
    y_levels <- levels(data[[y_col]])

    if (all(x_levels %in% y_levels) || all(y_levels %in% x_levels)) {
      # Determine the larger set of levels
      if (length(x_levels) >= length(y_levels)) {
        # Use x_col levels for sorting
        data[[x_col]] <- factor(data[[x_col]], levels = x_levels)
        data[[y_col]] <- factor(data[[y_col]], levels = x_levels)
      } else {
        # Use y_col levels for sorting
        data[[x_col]] <- factor(data[[x_col]], levels = y_levels)
        data[[y_col]] <- factor(data[[y_col]], levels = y_levels)
      }

      # Filter the data to keep only the lower triangle
      filtered_data <- data %>%
        filter(as.numeric(as.factor(!!sym(x_col))) > as.numeric(as.factor(!!sym(y_col))))
    } else {
      stop("The factor levels of x_col and y_col are not subsets of each other.")
    }
  } else {
    # Filter the data to keep only the lower triangle
    filtered_data <- data %>%
      filter(!!sym(x_col) > !!sym(y_col))
  }

  # Create the heatmap
  heatmap <- ggplot(filtered_data, aes_string(x = x_col, y = y_col, fill = fill_col)) +
    geom_tile() +
    scale_fill_gradient2(
      low = "blue", mid = "white", high = "red",
      midpoint = significant_val,
      limits = c(min_val, max_val)
    ) +
    theme_light() +
    theme(
      axis.text.x = element_text(angle = 45, hjust = 1, vjust = 0.5),
      axis.text.y = element_text(angle = 0, hjust = 1, vjust = 0.5),
      legend.position = "right",
      panel.grid = element_blank()
    ) +
    theme(plot.title = element_text(hjust = 0.5))

  # Add text annotations
  if (type == "cor") {
    heatmap <- heatmap +
      labs(x = "Model 1", y = "Model 2", fill = "Correlation") +
      geom_text(
        aes(label = ifelse(!!sym(fill_col) >= significant_val, "*",
          sprintf("%.4f", !!sym(fill_col))
        )),
        color = "black", size = 3
      )
  } else {
    heatmap <- heatmap +
      labs(x = "Model 1", y = "Model 2", fill = "Distance") +
      geom_text(
        aes(label = ifelse(!!sym(fill_col) <= significant_val, "*",
          sprintf("%.4f", !!sym(fill_col))
        )),
        color = "black", size = 3
      )
  }

  return(heatmap)
}

#' @description Create a violin plot with x-axis ordered by mean values and a red dot indicating the mean value.
#' @param data A data frame containing the data to be plotted.
#' @param x The name of the column to be used for the x-axis (factor).
#' @param y The name of the column to be used for the y-axis (numeric).
#' @param order The order in which to arrange the x-axis ("asc" for ascending, "desc" for descending).
#' @return A ggplot object representing the violin plot.
arranged_violin_plot <- function(data, x, y, order = "asc") {
  # Calculate the mean values for each factor level
  mean_values <- data %>%
    group_by({{ x }}) %>%
    summarize(mean_value = mean({{ y }}, na.rm = TRUE))

  # Arrange the mean values based on the specified order
  if (order == "asc") {
    mean_values <- mean_values %>% arrange(mean_value)
  } else if (order == "desc") {
    mean_values <- mean_values %>% arrange(desc(mean_value))
  } else {
    stop("Invalid order parameter. Use 'asc' for ascending or 'desc' for descending.")
  }

  # Reorder the factor levels based on the mean values
  data <- data %>%
    mutate({{ x }} := factor({{ x }}, levels = mean_values %>% pull({{ x }})))

  # Create the violin plot
  plot <- ggplot(data, aes(x = {{ x }}, y = {{ y }})) +
    geom_violin() +
    geom_point(data = mean_values, aes(x = {{ x }}, y = mean_value), color = "red", size = 2) +
    theme_light() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    labs(
      title = paste(deparse(substitute(y)), "distribution for all models"),
      x = "Model",
      y = deparse(substitute(y))
    )

  return(plot)
}

#' @description Create a violin plot with x-axis ordered by mean values and a red dot indicating the mean value,
#'              excluding categories with mean values below a specified threshold.
#' @param data A data frame containing the data to be plotted.
#' @param x The name of the column to be used for the x-axis (factor).
#' @param y The name of the column to be used for the y-axis (numeric).
#' @param threshold The threshold for the mean value below which categories will not be displayed.
#' @param order The order in which to arrange the x-axis ("asc" for ascending, "desc" for descending).
#' @return A ggplot object representing the violin plot.
arranged_violin_plot2 <- function(data, x, y, threshold, order = "asc") {
  # Calculate the mean values for each factor level
  mean_values <- data %>%
    group_by({{ x }}) %>%
    summarize(mean_value = mean({{ y }}, na.rm = TRUE))

  # Filter out the categories with mean values below the threshold
  mean_values_above_threshold <- mean_values %>%
    filter(mean_value >= threshold)

  # Arrange the mean values based on the specified order
  if (order == "asc") {
    mean_values_above_threshold <- mean_values_above_threshold %>% arrange(mean_value)
  } else if (order == "desc") {
    mean_values_above_threshold <- mean_values_above_threshold %>% arrange(desc(mean_value))
  } else {
    stop("Invalid order parameter. Use 'asc' for ascending or 'desc' for descending.")
  }

  # Reorder the factor levels based on the mean values and filter out the levels below the threshold
  data <- data %>%
    mutate({{ x }} := factor({{ x }}, levels = mean_values_above_threshold %>% pull({{ x }}))) %>%
    filter({{ x }} %in% levels({{ x }}))

  # Create the violin plot
  plot <- ggplot(data, aes(x = {{ x }}, y = {{ y }})) +
    geom_violin() +
    geom_point(data = mean_values_above_threshold, aes(x = {{ x }}, y = mean_value), color = "red", size = 2) +
    theme_light() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    labs(
      title = paste(deparse(substitute(y)), "distribution for all models (mean >= ", threshold, ")"),
      x = "Model",
      y = deparse(substitute(y))
    )

  return(plot)
}

# Example usage:
# arranged_violin_plot(all_models_dist, model2, Q_matrix.correlation, order = "desc")
# arranged_violin_plot2(all_models_dist, model2, Q_matrix.correlation, threshold = 0.5, order = "asc")

#' @description Generate a combined plot with a scatter plot in the middle and simple histograms on the left and top
#' @param data Data frame containing x and y columns
#' @param x Column name representing x-axis data
#' @param y Column name representing y-axis data
#' @param add_smooth Logical, whether to add a smooth line (default is TRUE)
#' @return ggplot object containing the combined plot
marginal_scatter_plot <- function(data, x, y, add_smooth = TRUE) {
  # Calculate the number of bins
  num_bins <- max(10, min(50, nrow(data) / 20))

  # Create scatter plot
  scatter_plot <- ggplot(data, aes_string(x = x, y = y)) +
    geom_point(color = "red", alpha = 0.6) +
    labs(x = "nRF distance", y = "Branch length difference (%)") +
    theme_minimal()

  # Add smooth line and annotations if add_smooth is TRUE
  if (add_smooth) {
    # Calculate correlation coefficient and regression formula
    correlation <- cor(data[[x]], data[[y]], method = "pearson")
    lm_model <- lm(data[[y]] ~ data[[x]])
    formula_text <- paste0("y = ", round(coef(lm_model)[1], 2), " + ", round(coef(lm_model)[2], 2), "x")
    correlation_text <- paste0("rho = ", round(correlation, 2), "\n", formula_text)

    scatter_plot <- scatter_plot +
      geom_smooth(method = "lm", color = "black", se = TRUE) +
      annotate("text", x = Inf, y = Inf, label = correlation_text, hjust = 1.1, vjust = 2.1, size = 5, color = "black")
  }

  # Add marginal histograms
  combined_plot <- ggMarginal(scatter_plot, type = "histogram", fill = "red", alpha = 0.6, bins = num_bins)

  return(combined_plot)
}

library(tidyverse)
library(ggplot2)
library(dendextend)

#' @description Generate a heatmap from a CSV file with hierarchical clustering
#' @param csv_path Path to the CSV file
#' @param value_col Column name for the values to be clustered
#' @param output_path Path to save the output heatmap
#' @param cluster_col1 Column name for the first tree
#' @param cluster_col2 Column name for the second tree
generate_heatmap <- function(csv_path, value_col, output_path, cluster_col1 = "Tree1", cluster_col2 = "Tree2") {
  # Read the CSV file
  summary_df <- read.csv(csv_path)
  
  # Create a symmetric dataframe
  summary_df_sym <- summary_df %>%
    rename(!!sym(cluster_col1) := !!sym(cluster_col2), !!sym(cluster_col2) := !!sym(cluster_col1))
  summary_df <- rbind(summary_df, summary_df_sym)
  
  # Create the distance matrix
  dist_matrix <- summary_df %>%
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
  summary_df <- summary_df %>%
    mutate(!!sym(cluster_col1) := factor(!!sym(cluster_col1), levels = hc$labels[hc$order]),
           !!sym(cluster_col2) := factor(!!sym(cluster_col2), levels = hc$labels[hc$order]))
  
  # Filter to only lower triangle
  summary_df <- summary_df %>%
    filter(as.numeric(!!sym(cluster_col1)) >= as.numeric(!!sym(cluster_col2)))
  
  # Generate heatmap
  heatmap <- ggplot(summary_df, aes_string(x = cluster_col1, y = cluster_col2, fill = value_col)) +
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
  
  num_x_labels <- length(hc$labels)
  # Calculate the width of the heatmap based on the number of x-axis labels
  fig_size <- num_x_labels / 1.5
  # Save the heatmap
  ggsave(output_path, heatmap, width = fig_size, height = fig_size)
}
