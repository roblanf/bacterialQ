# prune_subtree.R
library(castor)
library(ggplot2)
library(patchwork)
library(dplyr)
library(optparse)

FORCE_SIZE <- TRUE

#' Get interior nodes from a tree and calculate related parameters
#'
#' @param tree A phylogenetic tree object
#' @return A data frame containing interior nodes with calculated parameters
get_interior_nodes <- function(tree) {
  n_tip <- length(tree$tip)
  n_node <- length(tree$node.label)
  seq_along(tree$node.label) %>%
    data.frame(
      degree = count_tips_per_node(tree),
      node_id = .,
      mean_height_ct = get_all_node_depths(tree, as_edge_count = TRUE),
      mean_height_bl = get_all_node_depths(tree, as_edge_count = FALSE),
      red = get_reds(tree),
      depth_ct = get_all_distances_to_root(tree, as_edge_count = TRUE)[(n_tip + 1):(n_tip + n_node)],
      depth_bl = get_all_distances_to_root(tree, as_edge_count = FALSE)[(n_tip + 1):(n_tip + n_node)],
      father_node = get_ancestral_nodes(tree, . + n_tip, Nsplits = 1),
      node_label = tree$node.label
    ) %>%
    mutate(father_node = ifelse(father_node == node_id, 0, father_node)) %>%
    filter(degree > 1)
}

#' Filter interior nodes based on specified thresholds
#'
#' @param nodes A data frame containing interior nodes
#' @param min_degree Minimum degree threshold (default: 0)
#' @param max_degree Maximum degree threshold (default: Inf)
#' @param min_depth_bl Minimum depth (branch length) threshold (default: 0)
#' @param min_depth_ct Minimum depth (count) threshold (default: 0)
#' @param min_red Minimum RED threshold (default: 0)
#' @param max_red Maximum RED threshold (default: 1)
#' @return Filtered interior nodes
filter_nodes <- function(nodes, min_degree = 0, max_degree = Inf, min_depth_bl = 0, min_depth_ct = 0, min_red = 0, max_red = 1) {
  nodes %>%
    filter(
      degree >= min_degree, degree <= max_degree,
      depth_bl >= min_depth_bl, depth_ct >= min_depth_ct,
      red >= min_red, red <= max_red
    )
}

#' Plot histogram of data
#'
#' @param data A numeric vector of data
#' @param title Plot title
#' @param transform Transformation to apply to data (default: NULL)
#' @return A ggplot histogram
plot_histogram <- function(data, title, transform = NULL) {
  if (!is.null(transform)) {
    if (transform == "log2") {
      data <- log2(data)
      x_label <- paste("log2", title)
    } else if (transform == "sqrt") {
      data <- sqrt(data)
      x_label <- paste("sqrt", title)
    }
  } else {
    x_label <- title
  }

  data %>%
    data.frame() %>%
    ggplot(aes(x = data)) +
    geom_histogram(bins = 30, color = "black", fill = "white") +
    labs(title = title, x = x_label, y = "Frequency")
}

#' Analyze interior nodes and generate plots
#'
#' @param nodes A data frame containing interior nodes
#' @return A list containing combined plot and scatter plot
analyze_nodes <- function(nodes, degree_transform = "log2") {
  degree_plot <- plot_histogram(nodes$degree, "Degree Distribution", transform = degree_transform)
  red_plot <- plot_histogram(nodes$red, "Relative Evolutionary Divergence (RED) Distribution")
  depth_bl_plot <- plot_histogram(nodes$depth_bl, "Depth (Branch Length) Distribution")
  depth_ct_plot <- plot_histogram(nodes$depth_ct, "Depth (Count) Distribution")

  scatter_plot <- nodes %>%
    ggplot(aes(x = red, y = depth_bl, color = degree)) +
    geom_point(alpha = 0.5) +
    scale_color_gradientn(
      colors = c("blue", "red"), trans = "log2",
      name = "Degree",
      labels = function(x) x
    ) +
    labs(
      title = "RED vs. Depth (Branch Length)",
      x = "Relative Evolutionary Distance", y = "Depth (Branch Length)"
    )

  combined_plot <- (degree_plot | red_plot) / (depth_bl_plot | depth_ct_plot)

  return(list(
    combined_plot = combined_plot,
    scatter_plot = scatter_plot
  ))
}

#' Plot scatter comparison before and after pruning
#'
#' @param original_nodes A data frame containing original interior nodes
#' @param pruned_nodes A data frame containing pruned interior nodes
#' @return A ggplot scatter plot comparing before and after pruning
plot_scatter_comparison <- function(original_nodes, pruned_nodes) {
  scatter_plot <- original_nodes %>%
    ggplot(aes(x = red, y = depth_bl, color = degree)) +
    geom_point(alpha = 0.1, size = 0.5, color = "black") +
    labs(
      title = "RED vs. Depth (Branch Length)",
      x = "Relative Evolutionary Distance", y = "Depth (Branch Length)"
    )

  scatter_plot <- scatter_plot +
    geom_point(data = pruned_nodes, alpha = 1, size = 2) +
    scale_color_gradientn(
      colors = c("blue", "red"), trans = "log2",
      name = "Degree",
      labels = function(x) x
    )

  return(scatter_plot)
}

#' Select nodes to prune based on the degree strategy
#'
#' This function selects nodes to prune from the given tree based on the degree strategy.
#' It starts with the root node and iteratively selects the child nodes until all nodes
#' have a degree less than or equal to the maximum degree. Then, it replaces the nodes
#' with a degree greater than the minimum degree with their child nodes, starting from
#' the largest node, until the total number of taxa in the selected nodes reaches the
#' desired number or there are no more nodes to replace.
#'
#' @param nodes A data frame containing interior nodes
#' @param num_taxa Number of taxa to select (optional)
#' @param min_degree The minimum allowed degree for nodes
#' @param max_degree The maximum allowed degree for nodes
#' @return A data frame containing the selected nodes to prune
select_nodes_to_prune <- function(nodes, num_taxa = NULL, max_degree, min_degree) {
  # Select the root (filter node_id == 1)
  update_nodes <- nodes %>% filter(node_id == 1)
  # LOOP 1: Replace nodes with degree > max_degree with their child nodes
  while (any(update_nodes$degree > max_degree)) {
    cur_nodes <- update_nodes %>% filter(degree > max_degree)
    update_nodes <- update_nodes %>% filter(degree <= max_degree)
    child_nodes <- nodes %>% filter(father_node %in% cur_nodes$node_id)
    update_nodes <- bind_rows(update_nodes, child_nodes)
  }
  update_nodes <- update_nodes %>% filter(degree >= min_degree)

  # LOOP 2: Replace nodes with degree > min_degree with their child nodes
  while (all(update_nodes$degree >= min_degree)) {
    update_nodes_copy <- update_nodes
    if (is.null(num_taxa) && max(update_nodes_copy$degree) <= (1.5 * min_degree)) {
      return(update_nodes)
    }
    if (!is.null(num_taxa) && sum(update_nodes_copy$degree) >= num_taxa) {
      cur_nodes <- update_nodes_copy %>% filter(degree == max(degree))
      update_nodes_copy <- update_nodes_copy %>% filter(!(degree == max(degree)))
      child_nodes <- nodes %>%
        filter((father_node %in% cur_nodes$node_id) & (degree >= min_degree))
      if (nrow(child_nodes) == 0) {
        return(update_nodes)
      }
      update_nodes_copy <- bind_rows(update_nodes_copy, child_nodes)
    } else {
      return(update_nodes)
    }
    update_nodes <- update_nodes_copy
  }
  return(update_nodes)
}

#' Select nodes to prune based on the maximum depth length
select_nodes_by_criteria <- function(nodes, num_taxa = NULL, max_degree, min_degree) {
  pruned_nodes <- select_nodes_to_prune(nodes, num_taxa = NULL, max_degree, min_degree)
  pruned_nodes <- pruned_nodes %>% arrange(desc(depth_bl))

  if (!is.null(num_taxa)) {
    while (sum(pruned_nodes$degree) > num_taxa) {
      pruned_nodes <- pruned_nodes %>% slice(-n())
      if (sum(pruned_nodes$degree) < num_taxa) {
        break
      }
    }
  }

  return(pruned_nodes)
}

#' Perform automated pruning based on the total number of taxa and desired number of taxa
#'
#' @param tree A phylogenetic tree object
#' @param interior_nodes A data frame containing interior nodes
#' @param num_taxa Desired number of taxa
#' @param mode Pruning mode ("growth" or "criteria", default: "criteria")
#' @return A list containing the pruned nodes and pruning criteria
auto_prune <- function(tree, interior_nodes, num_taxa, mode = "criteria") {
  total_taxa <- length(tree$tip.label)
  taxa_num_min <- min(total_taxa, num_taxa)

  max_degree_set <- case_when(
    taxa_num_min >= 0 & taxa_num_min < 200 ~ 60,
    taxa_num_min >= 200 & taxa_num_min < 500 ~ 80,
    taxa_num_min >= 500 & taxa_num_min < 5000 ~ 79 + floor(taxa_num_min / 100),
    TRUE ~ 100
  )
  min_degree_set <- case_when(
    taxa_num_min >= 0 & taxa_num_min < 200 ~ 20,
    taxa_num_min >= 200 & taxa_num_min < 500 ~ 40,
    taxa_num_min >= 500 & taxa_num_min < 5000 ~ 39 + floor(taxa_num_min / 500),
    TRUE ~ 30
  )

  if (total_taxa <= max_degree_set) {
    return(list(pruned_nodes = interior_nodes %>% filter(node_id == 1), pruning_criteria = NULL))
  }

  if (mode == "growth") {
    pruned_nodes <- select_nodes_to_prune(interior_nodes, num_taxa, max_degree_set, min_degree_set)
  } else {
    pruned_nodes <- select_nodes_by_criteria(interior_nodes, num_taxa, max_degree_set)
  }
  if (FORCE_SIZE) {
    while (sum(pruned_nodes$degree) > num_taxa) {
      prev_pruned_nodes <- pruned_nodes
      pruned_nodes <- pruned_nodes %>%
        arrange(desc(degree)) %>%
        slice(-n())

      if (sum(pruned_nodes$degree) < num_taxa) {
        pruned_nodes <- prev_pruned_nodes
        break
      }
    }
  }

  return(pruned_nodes)
}

#' Output subtrees and taxa list
#'
#' @param tree A phylogenetic tree object
#' @param node_ids_to_prune A vector of node IDs to prune
#' @param output_dir Output directory
output_subtrees_and_taxa_list <- function(tree, node_ids_to_prune, output_dir) {
  if (!dir.exists(output_dir)) {
    dir.create(output_dir, recursive = TRUE)
  }

  taxa_list_dir <- paste0(output_dir, "/taxa_list")
  if (!dir.exists(taxa_list_dir)) {
    dir.create(taxa_list_dir, recursive = TRUE)
  }

  for (node in node_ids_to_prune) {
    subtree <- get_subtree_at_node(tree, node)$subtree
    taxa <- subtree$tip.label
    writeLines(taxa, con = paste0(taxa_list_dir, "/subtree_", node, ".txt"))
    write_tree(subtree, file = paste0(output_dir, "/subtree_", node, ".tre"))
  }
}

#' Main function to prune subtrees
#'
#' @param tree_file Path to the tree file
#' @param num_taxa Number of taxa to select
#' @param output_dir Output directory
#' @param mode Pruning mode ("growth" or "criteria", default: "criteria")
prune_subtrees <- function(tree_file, num_taxa, output_dir, mode = "criteria") {
  tree <- read_tree(file = tree_file)
  interior_nodes <- get_interior_nodes(tree)
  original_num_taxa <- length(tree$tip.label)

  pruned_nodes <- auto_prune(tree, interior_nodes, num_taxa, mode)
  summary_dir <- paste0(output_dir, "/summary")
  if (!dir.exists(summary_dir)) {
    dir.create(summary_dir, recursive = TRUE)
  }
  if (nrow(pruned_nodes) > 1) {
    original_summary <- analyze_nodes(interior_nodes)
    pruned_summary <- analyze_nodes(pruned_nodes, degree_transform = NULL)

    scatter_comparison <- plot_scatter_comparison(interior_nodes, pruned_nodes)
    plot_names <- c("original_combined_plot", "original_scatter_plot", "pruned_combined_plot", "pruned_scatter_plot", "scatter_comparison")
    plots <- list(
      original_summary$combined_plot, original_summary$scatter_plot,
      pruned_summary$combined_plot, pruned_summary$scatter_plot,
      scatter_comparison
    )

    for (i in seq_along(plot_names)) {
      ggsave(paste0(summary_dir, "/", plot_names[i], ".png"), plot = plots[[i]], width = 10, height = 8)
    }
  }

  node_ids_to_prune <- pruned_nodes$node_id
  output_subtrees_and_taxa_list(tree, node_ids_to_prune, output_dir)

  log_file <- paste0(summary_dir, "/prune_log.txt")
  log_info <- c(
    paste("Original number of taxa:", original_num_taxa),
    paste("Number of pruned subtrees:", length(node_ids_to_prune)),
    paste("Number of taxa after pruning:", sum(pruned_nodes$degree)),
    paste("Pruned node IDs:", paste(node_ids_to_prune, collapse = " ")),
    paste("Pruning mode:", mode)
  )
  writeLines(log_info, con = log_file)

  cat(log_info, sep = "\n")
  cat("Pruning completed. Results saved in", output_dir, "\n")
}


option_list <- list(
  make_option(c("-t", "--tree_file"), type = "character", default = NULL, help = "Path to the tree file", metavar = "character"),
  make_option(c("-n", "--num_taxa"), type = "integer", default = NULL, help = "Number of taxa", metavar = "integer"),
  make_option(c("-o", "--output_dir"), type = "character", default = "./subtree", help = "Path to the output directory", metavar = "character"),
  make_option(c("-m", "--mode"), type = "character", default = "growth", help = "Pruning mode (growth/criteria)", metavar = "character")
)

opt_parser <- OptionParser(option_list = option_list)
opt <- parse_args(opt_parser)

tree_file <- opt$tree_file
num_taxa <- opt$num_taxa
output_dir <- opt$output_dir
mode <- opt$mode

prune_subtrees(tree_file, num_taxa, output_dir, mode)
