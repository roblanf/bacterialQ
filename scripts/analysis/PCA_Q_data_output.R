#!/usr/bin/env Rscript

# Specify the output elements you want to generate
# output_elements <- c("PCA_R", "PCA_F", "PCA_Q") 
output_elements <- c("PCA_R", "PCA_F", "PCA_Q") 

args <- commandArgs(trailingOnly = TRUE)
existing_models_file <- args[1]
trained_models_file <- args[2]
output_directory <- args[3]

library(ggfortify)
library(ggrepel)

#' Calculate the normalization factor nu
#'
#' @param model A list containing R matrix and F vector
#' @return The normalization factor nu
get_nu <- function(model) {
  # Multiply R matrix by F vector
  Q_matrix <- model$R * model$F
  # Set diagonal elements to 0
  diag(Q_matrix) <- 0
  # Set diagonal elements to the negative sum of each row
  diag(Q_matrix) <- -rowSums(Q_matrix)
  # Calculate normalization factor nu using get_nu
  nu <- -1 / (diag(Q_matrix) * model$F)
  return(nu)
}

#' Convert R matrix and F vector to Q matrix
#'
#' @param model A list containing R matrix and F vector
#' @return The Q matrix
convert_Q <- function(model) {
  # Multiply R matrix by F vector
  Q_matrix <- model$R * model$F
  # Set diagonal elements to 0
  diag(Q_matrix) <- 0
  # Set diagonal elements to the negative sum of each row
  diag(Q_matrix) <- -rowSums(Q_matrix)
  # Calculate normalization factor nu using get_nu
  nu <- get_nu(model)
  # Multiply Q matrix by nu
  Q_matrix <- Q_matrix * nu
  diag(Q_matrix) <- NA
  Q_vector <- Q_matrix[!is.na(Q_matrix)]
  return(Q_vector)
}

convert_R_with_nu <- function(model) {
  R_matrix <- model$R
  # Calculate normalization factor nu using get_nu
  nu <- get_nu(model)
  # Multiply R matrix by nu
  R_matrix <- R_matrix * nu
  # Extract the lower triangular part of the matrix
  lower_tri_indices <- lower.tri(R_matrix, diag = FALSE)
  R_vector <- R_matrix[lower_tri_indices]
  return(R_vector)
}

#' Read models from a nexus file
#'
#' @param file_path The path to the nexus file
#' @return A list of models
read_nexus_models <- function(file_path) {
  nexus_lines <- readLines(file_path)
  model_start <- which(nexus_lines == "begin models;") + 1
  model_end <- which(nexus_lines == "end;") - 1
  model_lines <- nexus_lines[model_start:model_end]

  models <- list()
  i <- 1
  while (i <= length(model_lines)) {
    cur_line <- gsub("^\\s+|\\s+$", "", model_lines[i])
    if (grepl("^.*=$", model_lines[i])) {
      model_name <- gsub("=", "", model_lines[i])
      model_name <- gsub("^model", "", model_name)
      model_name <- gsub("^\\s+|\\s+$", "", model_name)
      R_matrix <- matrix(nrow = 20, ncol = 20)
      diag(R_matrix) <- 0
      for (j in 1:19) {
        i <- i + 1
        values <- as.numeric(strsplit(model_lines[i], " ")[[1]])
        if (length(values) == j) {
          R_matrix[j + 1, 1:j] <- values
        } else {
          warning(paste("Skipping line", i, "due to mismatch in values length for model", model_name))
        }
      }
      R_matrix[upper.tri(R_matrix)] <- t(R_matrix)[upper.tri(R_matrix)]
      i <- i + 1
      F_vector <- as.numeric(strsplit(gsub(";", "", model_lines[i]), " ")[[1]])
      models[[model_name]] <- list(name = model_name, R = R_matrix, F = F_vector)
    }
    i <- i + 1
  }
  return(models)
}

#' Determine the category of a model based on its name
#'
#' @param model_name The name of the model
#' @return The category of the model
determine_model_category <- function(model_name) {
  model_name <- toupper(model_name)
  
  if (grepl("P__", model_name)) {
    return("Bac_phyla")
  } else if (startsWith(model_name, "Q.BAC")) {
    return("Bac_General")
  } else if (startsWith(model_name, "MT")) {
    return("Mitochondria")
  } else if (startsWith(model_name, "CP")) {
    return("Chloroplast")
  } else if (startsWith(model_name, "HI") || startsWith(model_name, "FL") || endsWith(model_name, "REV")) {
    return("Virus")
  } else if (startsWith(model_name, "Q.")) {
    return("QMaker")
  } else {
    return("General")
  }
}

#' Perform PCA and generate plots and component files
#'
#' @param data The input data for PCA
#' @param data_type The type of data, used for file naming
#' @param output_directory The directory to save the output files
#' @param existing_model_list The list of existing models
generate_pca_output <- function(data, data_type, output_directory, existing_model_list) {
  # Determine file name suffix based on existing model list
  file_suffix <- if (length(existing_model_list) == 0) "_trained" else "" 

  # Perform PCA
  pca_result <- prcomp(data, scale. = TRUE)

  # Extract the first 10 principal components
  pca_components <- pca_result$x[, 1:10]

  # Combine model names with PCA components
  pca_components_df <- data.frame(
    Model = rownames(pca_components),
    pca_components
  )

  # # Write the raw data to csv file
  # write.csv(data, file.path(output_directory, paste0("PCA_", data_type, file_suffix, "_rawdata.csv")), row.names = TRUE)

  # Write the first 10 PCA components to csv file 
  write.csv(pca_components_df, file.path(output_directory, paste0("PCA_", data_type, file_suffix, "_components.csv")), row.names = FALSE)

  # Calculate and write the proportion of variance explained by each PC
  variance_explained <- pca_result$sdev^2 / sum(pca_result$sdev^2)
  write.csv(variance_explained, file.path(output_directory, paste0("PCA_", data_type, file_suffix, "_variance.csv")), row.names = TRUE)

  # Calculate and write the contribution of each variable to each PC
  pca_loadings <- pca_result$rotation[, 1:10]
  write.csv(pca_loadings, file.path(output_directory, paste0("PCA_", data_type, file_suffix, "_loadings.csv")), row.names = TRUE)

  # Create PCA plot using autoplot and add labels with geom_text_repel
  pca_plot <- autoplot(pca_result,
    data = data.frame(Model = rownames(data), Origin = model_origin, Category = model_category),
    colour = "Category", shape = "Origin"
  ) + 
    geom_text_repel(aes(label = Model), size = 3, show.legend = FALSE, max.overlaps = Inf) +
    scale_shape_manual(values = c(16, 8)) +
    labs(title = paste0("PCA of ", data_type)) +
    theme_bw() +
    theme(plot.title = element_text(hjust = 0.5))

  # Save PCA plot
  ggsave(filename = file.path(output_directory, paste0("PCA_", data_type, file_suffix, ".png")), plot = pca_plot, width = 12, height = 11, dpi = 300)
}


# ----- Main Script -----

# Read existing and trained models
if (file.exists(existing_models_file)) {
  existing_model_list <- read_nexus_models(existing_models_file)
} else {
  existing_model_list <- list()
}
trained_model_list <- read_nexus_models(trained_models_file)

# Extract data from models
existing_R_matrices <- lapply(existing_model_list, function(model) convert_R_with_nu(model))
trained_R_matrices <- lapply(trained_model_list, function(model) convert_R_with_nu(model))
existing_F_vectors <- lapply(existing_model_list, function(model) model$F)
trained_F_vectors <- lapply(trained_model_list, function(model) model$F)

# Combine data from existing and trained models
combined_R_matrices <- rbind(do.call(rbind, existing_R_matrices), do.call(rbind, trained_R_matrices))
combined_F_vectors <- rbind(do.call(rbind, existing_F_vectors), do.call(rbind, trained_F_vectors))

# Set row names for combined data
rownames(combined_R_matrices) <- c(names(existing_model_list), names(trained_model_list))
rownames(combined_F_vectors) <- c(names(existing_model_list), names(trained_model_list))

# Create a vector of model origins
model_origin <- c(rep("Existing", length(existing_model_list)), rep("Trained", length(trained_model_list)))

# Determine the category for each model
model_category <- sapply(rownames(combined_R_matrices), determine_model_category)

# Generate PCA output for R matrices if specified
if ("PCA_R" %in% output_elements) {
  generate_pca_output(combined_R_matrices, "R", output_directory, existing_model_list)
}

# Generate PCA output for F vectors if specified
if ("PCA_F" %in% output_elements) {
  generate_pca_output(combined_F_vectors, "F", output_directory, existing_model_list)
}

# Calculate and process Q matrices if specified
if ("PCA_Q" %in% output_elements) {
  # Calculate Q matrices for existing and trained models
  existing_Q_matrices <- lapply(existing_model_list, convert_Q)
  trained_Q_matrices <- lapply(trained_model_list, convert_Q)

  # Combine Q matrices
  combined_Q_matrices <- c(existing_Q_matrices, trained_Q_matrices)

  # Convert Q matrices to vectors
  combined_Q_vectors <- t(sapply(combined_Q_matrices, as.vector))

  # Set row names for Q vectors
  rownames(combined_Q_vectors) <- c(names(existing_model_list), names(trained_model_list))

  # Generate PCA output for Q matrices
  generate_pca_output(combined_Q_vectors, "Q", output_directory, existing_model_list)
}