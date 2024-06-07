library(tidyverse)

#' @description Generate a lower triangle heatmap
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
