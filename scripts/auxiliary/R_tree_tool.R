library(ape)

#' @description
#' Process the node labels of a tree. Ensure the right format of value.
#' @param tree A tree object read by the ape package.
#' @return A tree object with processed node labels.
standardize_node_labels <- function(tree) {
  # Convert node labels to numeric
  node_labels <- as.numeric(tree$node.label)
  # Replace NA values with 100
  node_labels[is.na(node_labels)] <- 0
  # Check if the mean of numeric labels is less than 1
  if (mean(node_labels, na.rm = TRUE) > 1) {
    node_labels <- ceiling(node_labels)
  } else {
    node_labels <- round(node_labels, 2)
  }

  # Convert back to character and replace the original labels
  tree$node.label <- as.character(node_labels)
    
  return(tree)
}


#' @description
#' Separate a tree into PP (Posterior Probability) and BS (Bootstrap Support) trees
#' based on the node labels. The function splits the labels and assigns them accordingly.
#' @param tree A tree object read by the ape package.
#' @return A list containing 'PP' and 'BS' trees with standardized node labels.
seperate_node_label <- function(tree) {
 
  # Check if any separator exists in the node labels
  if (any(grepl("/", tree$node.label))) {
    support_sep <- "/"
  } else if (any(grepl("\\|", tree$node.label))) {
    support_sep <- "|"
  } else {
    support_sep <- NULL
  }
  
  if (!is.null(support_sep)) {
    # Split the node labels into two parts based on the separator
    split_labels <- strsplit(tree$node.label, support_sep)
    PP_labels <- sapply(split_labels, `[`, 1)
    BS_labels <- sapply(split_labels, `[`, 2)
    
    # Create two copies of the tree
    PP_tree <- tree
    BS_tree <- tree
    
    # Assign the split labels to the respective trees
    PP_tree$node.label <- PP_labels
    BS_tree$node.label <- BS_labels
    
    # Standardize the node labels in both trees
    PP_tree <- standardize_node_labels(PP_tree)
    BS_tree <- standardize_node_labels(BS_tree)
    
    # Determine which tree is PP and which is BS based on the mean of the labels
    if (mean(as.numeric(PP_tree$node.label), na.rm = TRUE) < 1) {
      result <- list(PP = PP_tree, BS = BS_tree)
    } else {
      result <- list(PP = BS_tree, BS = PP_tree)
    }
  } else {
    # No separator found, so determine if it's a PP or BS tree based on the mean of the labels
    node_labels <- as.numeric(tree$node.label)
    label_mean <- mean(node_labels, na.rm = TRUE)
    
    if (!is.na(label_mean)) {
      if (label_mean <= 1) {
        PP_tree <- standardize_node_labels(tree)
        result <- list(PP = PP_tree)
      } else {
        BS_tree <- standardize_node_labels(tree)
        result <- list(BS = BS_tree)
      }
    } else {
      # No valid labels found
      result <- list()
    }
  }
  
  return(result)
}

#' @description
#' Ensure two trees have the same label type, either PP (Posterior Probability) or BS (Bootstrap Support).
#' @param tree1 First tree object read by the ape package.
#' @param tree2 Second tree object read by the ape package.
#' @return A list containing the two trees and the type of label used ("PP" or "BS").
keep_same_tree_label <- function(tree1, tree2) {
    
  # Process node labels for both trees
  label1 <- seperate_node_label(tree1)
  label2 <- seperate_node_label(tree2)
  
  # Determine the type to use based on the labels available
  if (length(label1$BS) > 0 && length(label2$BS) > 0) {
    type <- "BS"
  } else if (length(label1$PP) > 0 && length(label2$PP) > 0) {
    type <- "PP"
  } else {
    type <- "NULL"
  }
  
  if (type == "NULL") {
    tree1$node.label <- NULL
    tree2$node.label <- NULL
  } else{
    # Assign the selected type to both trees
    tree1 <- if (type == "BS") label1$BS else label1$PP
    tree2 <- if (type == "BS") label2$BS else label2$PP
  }
  
  return(list(tree1 = tree1, tree2 = tree2, type = type))
}

# Function to check and standardize tree properties (taxa labels and rooting)
#' @description Checks if two trees have the same taxa and makes sure they are unrooted.
#' If taxa differ, the differing taxa are dropped from both trees.
#' @param tree1 First tree object
#' @param tree2 Second tree object
#' @return A list containing two modified tree objects.
standardize_trees <- function(tree1, tree2) {
  # Unroot trees if either tree is rooted
  if (is.rooted(tree1) || is.rooted(tree2)) {
    tree1 <- unroot(tree1)
    tree2 <- unroot(tree2)
  }

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
