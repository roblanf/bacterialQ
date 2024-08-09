library(ape)

process_node_labels <- function(tree) {
  #' @description
  #' Process the node labels of a tree. Convert labels to numeric, scale if mean is less than 1, and convert back to character.
  #' @param tree A tree object read by the ape package.
  #' @return A tree object with processed node labels.

  # Convert node labels to numeric
  node_labels <- as.numeric(tree$node.label)

  # Check if the mean of numeric labels is less than 1
  if (mean(node_labels, na.rm = TRUE) < 1) {
    # Scale the labels by 100 and convert to integer
    node_labels <- as.integer(node_labels * 100)
  }

  # Convert back to character and replace the original labels
  tree$node.label <- as.character(node_labels)

  return(tree)
}

# Function to check and standardize tree properties (taxa labels and rooting)
#' @description Checks if two trees have the same taxa and makes sure they are unrooted.
#' If taxa differ, the differing taxa are dropped from both trees.
#' @param tree1 First tree object
#' @param tree2 Second tree object
#' @return A list containing two modified tree objects.
standardize_trees <- function(tree1, tree2) {
  # Check if the taxa of the two trees are equal
  taxa_equal <- setequal(tree1$tip.label, tree2$tip.label)
  if (!taxa_equal) {
    taxa_diff1 <- setdiff(tree1$tip.label, tree2$tip.label)
    taxa_diff2 <- setdiff(tree2$tip.label, tree1$tip.label)
    warning(
      "The taxa of the two trees are not equal.\n",
      "Number of taxa unique to Tree 1: ", length(taxa_diff1), "\n",
      "Number of taxa unique to Tree 2: ", length(taxa_diff2), "\n",
      "The differing taxa have been removed for the analysis.\n"
    )
    tree1 <- drop.tip(tree1, taxa_diff1)
    tree2 <- drop.tip(tree2, taxa_diff2)
  }
  
  # Unroot trees if rooted
  if (is.rooted(tree1)) {
    tree1 <- unroot(tree1)
  }
  if (is.rooted(tree2)) {
    tree2 <- unroot(tree2)
  }

  return(list(tree1 = tree1, tree2 = tree2))
}

# Function to calculate tree distances
#' @description Calculates a set of tree distance metrics between two trees.
#' @param tree1 First tree object
#' @param tree2 Second tree object
#' @return A data frame containing calculated distance metrics.
calculate_tree_distances <- function(tree1, tree2) {

  library(phangorn)
  # Standardize trees
  standardized_trees <- standardize_trees(tree1, tree2)
  tree1 <- standardized_trees$tree1
  tree2 <- standardized_trees$tree2

  # Calculate distances
  RF_dist <- round(RF.dist(tree1, tree2, normalize = FALSE, check.labels = TRUE), 4)
  nRF_dist <- round(RF.dist(tree1, tree2, normalize = TRUE, check.labels = TRUE), 4)
  wRF_dist <- round(wRF.dist(tree1, tree2, normalize = FALSE, check.labels = TRUE), 4)
  KF_dist <- round(KF.dist(tree1, tree2, check.labels = TRUE), 4)
  SPR_dist <- round(SPR.dist(tree1, tree2), 4)
  path_dist <- round(path.dist(tree1, tree2, check.labels = TRUE, use.weight = TRUE), 4)

  # Calculate tree lengths
  tree1_bl <- sum(tree1$edge.length)
  tree2_bl <- sum(tree2$edge.length)
  bl_diff_pct <- (tree2_bl - tree1_bl) / tree1_bl * 100

  # Create a data frame with the results
  data.frame(
    "RF_dist" = RF_dist,
    "nRF" = nRF_dist,
    "wRF" = wRF_dist,
    "KF_dist" = KF_dist,
    "SPR_dist" = SPR_dist,
    "Path_dist" = path_dist,
    "Tree1_BL" = tree1_bl,
    "Tree2_BL" = tree2_bl,
    "BL_diff_per" = bl_diff_pct
  )
}
