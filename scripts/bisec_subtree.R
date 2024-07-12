# Load necessary libraries
library(ape)
library(phangorn)

# @description
# This function finds the edge that linked to root by read the tree$edge matrix.
# @param tree A phylo format phylogenetic tree.
# @return A vector of unique integers that represent the node number that linked to root.
find_root_edge <- function(tree) {
  # Get the edge matrix
  matrix <- tree$edge
  root_node <- 1 + length(tree$tip.label)

  # Extract all rows that contain the number 1
  rows_with_one <- matrix[apply(matrix, 1, function(row) any(row == root_node)), ]
  # Flatten the matrix to a vector
  numbers <- as.vector(rows_with_one)
  # Get unique numbers
  unique_numbers <- unique(numbers)
  # Remove the number 1
  result <- unique_numbers[unique_numbers != root_node]

  return(result)
}

#' @description Process a phylogenetic tree by repeatedly rooting at the midpoint and splitting until all subtrees are within the specified size limits.
#' @param tree_file Path to the Newick file containing the phylogenetic tree.
#' @param tree_size_lower_lim Minimum size of the subtrees to keep.
#' @param tree_size_upper_lim Maximum size of the subtrees to split.
#' @param output_dir Directory to save the processed subtrees.
process_phylogenetic_tree <- function(tree_file, tree_size_lower_lim, tree_size_upper_lim, output_dir) {
  # Read the tree from the file
  unsolve_subtree_list <- list(read.tree(tree_file))
  solved_subtree_list <- list()
  process_tree_list <- list()

  # Loop until unsolve_subtree_list is empty
  while (length(unsolve_subtree_list) > 0) {
    for (tree in unsolve_subtree_list) {
      # Check the size of the tree
      tree_size <- length(tree$tip.label)
      if (tree_size < tree_size_lower_lim) {
        # Discard the tree if it's too small
        next
      } else if (tree_size <= tree_size_upper_lim) {
        # Keep the tree if it's within the size limits
        solved_subtree_list <- append(solved_subtree_list, list(tree))
      } else {
        # Process the tree if it's too large
        tree <- midpoint(tree, node.labels = "support")
        # Extract subtrees
        root_edge_nodes <- find_root_edge(tree)
        subtree1 <- extract.clade(tree, root_edge_nodes[[1]], collapse.singles = TRUE)
        subtree2 <- extract.clade(tree, root_edge_nodes[[2]], collapse.singles = TRUE)
        process_tree_list <- append(process_tree_list, list(subtree1, subtree2))
      }
    }
    # Replace unsolve_subtree_list with process_tree_list and clear process_tree_list
    unsolve_subtree_list <- process_tree_list
    process_tree_list <- list()
  }

  # Save the solved subtrees to the output directory
  for (i in seq_along(solved_subtree_list)) {
    write.tree(solved_subtree_list[[i]], file = file.path(output_dir, paste0("subtree_", i, ".nwk")))
  }
}

#' Output subtrees and taxa list
#'
#' @param subtree_list
#' @param output_dir Output directory
output_subtrees_and_taxa_list <- function(subtree_list, output_dir) {
  if (!dir.exists(output_dir)) {
    dir.create(output_dir, recursive = TRUE)
  }

  taxa_list_dir <- paste0(output_dir, "/taxa_list")
  if (!dir.exists(taxa_list_dir)) {
    dir.create(taxa_list_dir, recursive = TRUE)
  }

  for (subtree in subtree_list) {
    taxa <- subtree$tip.label
    writeLines(taxa, con = paste0(taxa_list_dir, "/subtree_", node, ".txt"))
    write_tree(subtree, file = paste0(output_dir, "/subtree_", node, ".tre"))
  }
}


process_phylogenetic_tree(tree_file = "/home/tim/project/GTDB_TREE/Result_rona/test/p__Marinisomatota_275/ref_tree.tre", tree_size_lower_lim = 3, tree_size_upper_lim = 30, output_dir = "/home/tim/project/GTDB_TREE/Result_rona/test/p__Marinisomatota_275/loop_1/mid_point_trees")
