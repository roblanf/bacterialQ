# prune_subtree.R
library(castor)
library(ggplot2)
library(patchwork)
library(dplyr)
library(optparse)
library(ape)

#' Get interior nodes from a tree and calculate related parameters
#'
#' @param tree A phylogenetic tree object
#' @return A data frame containing interior nodes with calculated parameters
get_interior_nodes <- function(tree) {
  n_tip <- length(tree$tip)
  n_node <- length(tree$node.label)
  seq_along(tree$node.label) %>%
    tibble(
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
    filter(degree > 3)
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
    tibble() %>%
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

#' Split function to select nodes to prune
#'
#' @param candidate_nodes A data frame containing candidate nodes
#' @param all_nodes A data frame containing all available nodes
#' @param tree_size_lower_lim Lower limit for the size of subtrees
#' @param tree_size_upper_lim Upper limit for the size of subtrees
#' @param num_tree Number of subtrees to select (optional)
#' @param mode Splitting mode (0, 1, 2, or 3)
#' @return A vector of node IDs to prune
split_func <- function(candidate_nodes, all_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree = NULL, mode = 1) {
  if (mode == 0) {
    # Return nodes with degree > tree_size_upper_lim
    candidate_nodes %>%
      filter(degree > tree_size_upper_lim) %>%
      pull(node_id)
  } else {
    # Add a column to candidate_nodes indicating the degree of their child nodes
    candidate_nodes <- candidate_nodes %>%
      filter(node_id %in% all_nodes$father_node) %>%
      left_join(all_nodes, by = c("node_id" = "father_node")) %>%
      group_by(node_id) %>%
      summarise(
        child_degrees = list(degree.y),
        depth_bl = first(depth_bl.x),
        degree = first(degree.x)
      ) %>%
      mutate(child_degrees = lapply(child_degrees, as.integer)) %>% # Convert child_degrees to integer
      filter(sapply(child_degrees, function(x) any(x >= tree_size_lower_lim))) # Filter nodes with child_degrees >= tree_size_lower_lim

    if (mode == 1) {
      # Return the nodes with at least one child node having degree >= tree_size_lower_lim
      candidate_nodes %>%
        pull(node_id)
    } else if (mode == 2) {
      # Return the node with the child node having the maximum degree >= tree_size_lower_lim
      candidate_nodes %>%
        mutate(max_child_degree = sapply(child_degrees, max)) %>%
        arrange(desc(max_child_degree)) %>%
        slice(1) %>%
        pull(node_id)
    } else if (mode == 3) {
      # Return the node with the minimal depth(branch length) and at least one child node having degree >= tree_size_lower_lim
      candidate_nodes %>%
        arrange(depth_bl) %>%
        slice(1) %>%
        pull(node_id)
    }
  }
}

#' Split nodes based on a list of node IDs to remove
#'
#' @param nodes A data frame containing current nodes
#' @param all_nodes A data frame containing all interior nodes
#' @param node_ids_to_remove A vector of node IDs to remove
#' @return A data frame containing the updated nodes
split_nodes <- function(nodes, all_nodes, node_ids_to_remove, tree_size_lower_lim) {
  retained_nodes <- nodes[!(nodes$node_id %in% node_ids_to_remove), ]
  update_nodes <- nodes[(nodes$node_id %in% node_ids_to_remove), ]
  child_nodes <- all_nodes[all_nodes$father_node %in% update_nodes$node_id, ]

  updated_nodes <- bind_rows(retained_nodes, child_nodes) %>%
    filter(degree >= tree_size_lower_lim)

  return(updated_nodes)
}

#' Select nodes to prune based on the specified strategy
#'
#' @param all_nodes A data frame containing all interior nodes
#' @param tree_size_lower_lim Lower limit for the size of subtrees
#' @param tree_size_upper_lim Upper limit for the size of subtrees
#' @param num_tree Number of subtrees to select (optional)
#' @param mode Splitting mode (0, 1, 2, or 3)
#' @return A data frame containing the selected nodes to prune
select_nodes_to_prune <- function(all_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree = NULL, mode = 1) {
  # Initial pruning: remove nodes with degree > tree_size_upper_lim
  candidate_nodes <- all_nodes[all_nodes$node_id == 1, ]

  while (TRUE) {
    node_ids_to_prune <- split_func(candidate_nodes, all_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree, mode = 0)
    if (length(node_ids_to_prune) == 0) {
      break
    }
    candidate_nodes <- split_nodes(candidate_nodes, all_nodes, node_ids_to_prune, tree_size_lower_lim)
  }
  if (mode == 0) {
    return(candidate_nodes)
  }
  # Further pruning based on the specified mode
  while (TRUE) {
    node_ids_to_prune <- split_func(candidate_nodes, all_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree, mode)
    if (length(node_ids_to_prune) == 0 || (!is.null(num_tree) && nrow(candidate_nodes) >= num_tree)) {
      break
    }
    candidate_nodes <- split_nodes(candidate_nodes, all_nodes, node_ids_to_prune, tree_size_lower_lim)
  }
  return(candidate_nodes)
}


#' Perform automated pruning based on the total number of taxa and desired number of taxa
#'
#' @param tree A phylogenetic tree object
#' @param interior_nodes A data frame containing interior nodes
#' @param tree_size_lower_lim Lower limit for the size of subtrees
#' @param tree_size_upper_lim Upper limit for the size of subtrees
#' @param num_tree Number of subtrees to select (optional)
#' @param mode Pruning mode ("random", "lower", "upper", or "shallow")
#' @return A list containing the pruned nodes and pruning criteria
auto_prune <- function(tree, interior_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree = NULL, mode = "random") {
  total_taxa <- length(tree$tip.label)

  if (mode == "random") {
    pruned_nodes <- select_nodes_to_prune(interior_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree, mode = 0)
    if (!is.null(num_tree)) {
      if (nrow(pruned_nodes) >= num_tree) {
        pruned_nodes <- pruned_nodes %>% sample_n(num_tree)
      }
    }
  } else if (mode == "lower") {
    pruned_nodes <- select_nodes_to_prune(interior_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree = NULL, mode = 1)
    if (!is.null(num_tree)) {
      if (nrow(pruned_nodes) >= num_tree) {
        pruned_nodes <- pruned_nodes %>%
          arrange(degree) %>%
          slice(1:num_tree)
      }
    }
  } else if (mode == "upper") {
    pruned_nodes <- select_nodes_to_prune(interior_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree, mode = 2)
    if (!is.null(num_tree)) {
      if (nrow(pruned_nodes) >= num_tree) {
        pruned_nodes <- pruned_nodes %>%
          arrange(desc(degree)) %>%
          slice(1:num_tree)
      }
    } else {
      # keep nodes to the sum up top 80% degree count from high to low
      total_taxa <- interior_nodes %>%
        filter(node_id == 1) %>%
        pull(degree)
      pruned_nodes <- pruned_nodes %>%
        arrange(desc(degree)) %>%
        mutate(cum_degree = cumsum(degree)) %>%
        filter(cum_degree <= 0.8 * total_taxa)
    }
  } else if (mode == "shallow") {
    pruned_nodes <- select_nodes_to_prune(interior_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree = NULL, mode = 3)
    if (!is.null(num_tree)) {
      if (nrow(pruned_nodes) >= num_tree) {
        pruned_nodes <- pruned_nodes %>%
          arrange(desc(depth_bl)) %>%
          slice(1:num_tree)
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
    subtree <- extract.clade(tree, node + length(tree$tip.label), collapse.singles = TRUE)
    taxa <- subtree$tip.label
    writeLines(taxa, con = paste0(taxa_list_dir, "/subtree_", node, ".txt"))
    write_tree(subtree, file = paste0(output_dir, "/subtree_", node, ".tre"))
  }
}

#' Main function to prune subtrees
#'
#' @param tree_file Path to the tree file
#' @param tree_size_lower_lim Lower limit for the size of subtrees
#' @param tree_size_upper_lim Upper limit for the size of subtrees
#' @param num_tree Number of subtrees to select (optional)
#' @param output_dir Output directory
#' @param mode Pruning mode ("random", "lower", "upper", or "shallow")
prune_subtrees <- function(tree_file, tree_size_lower_lim, tree_size_upper_lim, num_tree = NULL, output_dir, mode = "random") {
  # Read and process the input tree
  tree <- read_tree(file = tree_file) %>%
    root_at_midpoint()

  interior_nodes <- get_interior_nodes(tree)
  original_num_taxa <- length(tree$tip.label)

  # Perform automated pruning based on the specified mode
  pruned_nodes <- auto_prune(tree, interior_nodes, tree_size_lower_lim, tree_size_upper_lim, num_tree, mode) %>%
    arrange(desc(degree))

  # Create summary directory if it doesn't exist
  summary_dir <- paste0(output_dir, "/summary")
  if (!dir.exists(summary_dir)) {
    dir.create(summary_dir, recursive = TRUE)
  }

  # Generate summary plots if more than one pruned node
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

    # Save summary plots using a for loop
    for (i in seq_along(plot_names)) {
      ggsave(paste0(summary_dir, "/", plot_names[i], ".png"), plot = plots[[i]], width = 10, height = 8)
    }
  }

  # Get the node IDs to prune
  node_ids_to_prune <- pruned_nodes$node_id

  # Output subtrees and taxa list
  output_subtrees_and_taxa_list(tree, node_ids_to_prune, output_dir)

  # Create log file with pruning information
  log_file <- paste0(summary_dir, "/prune_log.txt")
  log_info <- c(
    paste("Original number of taxa:", original_num_taxa, "  "),
    paste("Number of pruned subtrees:", length(node_ids_to_prune), "  "),
    paste("Number of taxa after pruning:", sum(pruned_nodes$degree), "  "),
    paste("Pruned node IDs (degree):", paste(sprintf("%d (%d)", node_ids_to_prune, pruned_nodes$degree), collapse = " "), "  "),
    paste("Pruning mode:", mode, "  ")
  )
  writeLines(log_info, con = log_file)

  # Print log information and completion message
  cat(log_info, sep = "\n")
  cat("Pruning completed. Results saved in", output_dir, "\n")
}

# Define command-line options
option_list <- list(
  make_option(c("-t", "--tree_file"), type = "character", default = NULL, help = "Path to the tree file", metavar = "character"),
  make_option(c("-l", "--tree_size_lower_lim"), type = "integer", default = 20, help = "Lower limit for the size of subtrees", metavar = "integer"),
  make_option(c("-u", "--tree_size_upper_lim"), type = "integer", default = 100, help = "Upper limit for the size of subtrees", metavar = "integer"),
  make_option(c("-n", "--num_tree"), type = "integer", default = NULL, help = "Number of subtrees", metavar = "integer"),
  make_option(c("-o", "--output_dir"), type = "character", default = "./subtree", help = "Path to the output directory", metavar = "character"),
  make_option(c("-m", "--mode"), type = "character", default = "random", help = "Pruning mode (random/lower/upper/shallow)", metavar = "character")
)

# Parse command-line options
opt_parser <- OptionParser(option_list = option_list)
opt <- parse_args(opt_parser)

# Extract command-line arguments
tree_file <- opt$tree_file
tree_size_lower_lim <- opt$tree_size_lower_lim
tree_size_upper_lim <- opt$tree_size_upper_lim
num_tree <- opt$num_tree
output_dir <- opt$output_dir
mode <- opt$mode

# Call the main function with command-line arguments
prune_subtrees(tree_file, tree_size_lower_lim, tree_size_upper_lim, num_tree, output_dir, mode)
