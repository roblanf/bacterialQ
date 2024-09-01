#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
existing_model_nex <- args[1]
trained_model_nex <- args[2]
output_dir <- args[3]

library(ggfortify)
library(ggrepel)
library(Rtsne)

#' Read Q matrix and convert it to a vector
#'
#' @param Q_matrix The Q matrix
#' @return The Q matrix as a vector
readQ <- function(Q_matrix) {
  Q <- (Q_matrix + t(Q_matrix))
  diag(Q) <- 0
  Q <- (Q / sum(Q)) * 100.0
  Q <- Q[lower.tri(Q)]
  return(as.vector(Q))
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
      Q_matrix <- matrix(nrow = 20, ncol = 20)
      diag(Q_matrix) <- 0
      for (j in 1:19) {
        i <- i + 1
        values <- as.numeric(strsplit(model_lines[i], " ")[[1]])
        if (length(values) == j) {
          Q_matrix[j + 1, 1:j] <- values
        } else {
          warning(paste("Skipping line", i, "due to mismatch in values length for model", model_name))
        }
      }
      Q_matrix[upper.tri(Q_matrix)] <- t(Q_matrix)[upper.tri(Q_matrix)]
      i <- i + 1
      F_vector <- as.numeric(strsplit(gsub(";", "", model_lines[i]), " ")[[1]])
      models[[model_name]] <- list(name = model_name, Q = Q_matrix, F = F_vector)
    }
    i <- i + 1
  }
  return(models)
}

# Read existing and trained models
if (file.exists(existing_model_nex)) {
  existing_models <- read_nexus_models(existing_model_nex)
} else {
  existing_models <- list()
}
trained_models <- read_nexus_models(trained_model_nex)

# Extract Q matrices and F vectors from existing models
exist_Q <- lapply(existing_models, function(model) readQ(model$Q))
exist_F <- lapply(existing_models, function(model) model$F)

# Extract Q matrices and F vectors from trained models
trained_Q <- lapply(trained_models, function(model) readQ(model$Q))
trained_F <- lapply(trained_models, function(model) model$F)

# Combine Q matrices and F vectors from existing and trained models
allQ <- rbind(do.call(rbind, exist_Q), do.call(rbind, trained_Q))
allF <- rbind(do.call(rbind, exist_F), do.call(rbind, trained_F))

# Set row names
rownames(allQ) <- c(names(existing_models), names(trained_models))
rownames(allF) <- c(names(existing_models), names(trained_models))

# Check if there are at least two models
if (nrow(allQ) < 2 || nrow(allF) < 2) {
  stop("There must be at least two models.")
}

# Create a vector of model sources
model_source <- c(rep("Existing", length(existing_models)), rep("Trained", length(trained_models)))

#' Determine the category of a model based on its name
#'
#' @param model_name The name of the model
#' @return The category of the model
determine_type <- function(model_name) {
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

# Determine the type for each model
model_type <- sapply(rownames(allQ), determine_type)
perp <- min(floor((nrow(allQ) - 1) / 3), 5)
# Perform t-SNE on the data
tsne_Q <- Rtsne(allQ, dims = 2, perplexity = perp, check_duplicates = FALSE, initial_dims = 50, theta = 0.1)
tsne_F <- Rtsne(allF, dims = 2, perplexity = perp, check_duplicates = FALSE, initial_dims = 20, theta = 0.1)


# Create t-SNE plot for Q matrices using ggplot and add labels with geom_text_repel
plot_data <- data.frame(
  tSNE1 = tsne_Q$Y[, 1],
  tSNE2 = tsne_Q$Y[, 2],
  Model = rownames(allQ),
  Source = model_source,
  Type = model_type
)

tsne_Q_plot <- ggplot(plot_data, aes(x = tSNE1, y = tSNE2, color = Type, shape = Source)) +
  geom_point() +
  geom_text_repel(aes(label = Model), size = 3, show.legend = FALSE, max.overlaps = Inf, parse = TRUE) +
  scale_shape_manual(values = c(16, 8)) +
  labs(title = "t-SNE of Q matrices") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))

# Save t-SNE plot for Q matrices
# if existing_models is empty, then change the name of plot
if (length(existing_models) == 0) {
  ggsave(filename = file.path(output_dir, "tSNE_Q_trained.png"), plot = tsne_Q_plot, width = 12, height = 11, dpi = 300)
} else {
  ggsave(filename = file.path(output_dir, "tSNE_Q.png"), plot = tsne_Q_plot, width = 12, height = 11, dpi = 300)
}

# Create t-SNE plot for stationary frequencies using ggplot and add labels with geom_text_repel
tsne_F_plot <- ggplot(data.frame(tSNE1 = tsne_F$Y[, 1], tSNE2 = tsne_F$Y[, 2], Model = rownames(allQ), Source = model_source, Type = model_type), aes(x = tSNE1, y = tSNE2, color = Type, shape = Source)) +
  geom_point() +
  geom_text_repel(aes(label = Model), size = 3, show.legend = FALSE, max.overlaps = Inf) +
  scale_shape_manual(values = c(16, 8)) +
  labs(title = "t-SNE of stationary frequencies") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))

# Save t-SNE plot for stationary frequencies
if (length(existing_models) == 0) {
  ggsave(filename = file.path(output_dir, "tSNE_F_trained.png"), plot = tsne_F_plot, width = 12, height = 11, dpi = 300)
} else {
  ggsave(filename = file.path(output_dir, "tSNE_F.png"), plot = tsne_F_plot, width = 12, height = 11, dpi = 300)
}
