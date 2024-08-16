# Load required libraries
library(ape)
library(phangorn)

# Define a function to extract the tree name from the file path
extract_tree_name <- function(file_path) {
  # Remove the directory path and file extension from the file path
  tree_name <- sub("^.*\\/", "", file_path)
  tree_name <- sub("\\..*$", "", tree_name)
  return(tree_name)
}


# Define a function to calculate distance metrics between two trees
calculate_tree_distances <- function(tree1_path, tree2_path, summary_path) {
  # Read tree files
  tree1 <- read.tree(tree1_path)
  tree2 <- read.tree(tree2_path)
  
  # Extract tree names from file paths
  tree1_name <- extract_tree_name(tree1_path)
  tree2_name <- extract_tree_name(tree2_path)
  
  # Calculate distances
  RF_dist <- round(RF.dist(tree1, tree2, normalize = FALSE, check.labels = TRUE, rooted = FALSE), 4)
  nRF_dist <- round(RF.dist(tree1, tree2, normalize = TRUE, check.labels = TRUE, rooted = FALSE), 4)
  wRF_dist <- round(wRF.dist(tree1, tree2, normalize = FALSE, check.labels = TRUE, rooted = FALSE), 4)
  KF_dist <- round(KF.dist(tree1, tree2, check.labels = TRUE, rooted = FALSE), 4)
  SPR_dist <- round(SPR.dist(tree1, tree2), 4)
  path_dist <- round(path.dist(tree1, tree2, check.labels = TRUE, use.weight = TRUE), 4)
  
  # Calculate tree lengths
  tree1_bl <- sum(tree1$edge.length)
  tree2_bl <- sum(tree2$edge.length)
  bl_diff_pct <- (tree2_bl - tree1_bl) / tree1_bl * 100
  
  # Create a data frame with the results
  result_df <- data.frame(
    "Tree1" = tree1_name,
    "Tree2" = tree2_name,
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
  
  # If the csv file doesn't exist or is empty, write the column names
  if (!file.exists(summary_path) || file.size(summary_path) == 0) {
    write.table(result_df, file = summary_path, sep = ",", row.names = FALSE, col.names = TRUE)
  } else {
    # If the csv file exists and is not empty, append the results (without column names)
    write.table(result_df, file = summary_path, sep = ",", row.names = FALSE, col.names = FALSE, append = TRUE)
  }
  
  # Return the result data frame
  return(result_df)
}

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 3) {
  stop("Usage: Rscript script.R <tree1_path> <tree_folder> <summary_path>")
}

# Assign command line arguments to variables
tree1_path <- args[1]
tree_folder <- args[2]
summary_path <- args[3]

# Get a list of tree files in the folder
tree_files <- list.files(tree_folder, full.names = TRUE)

# Loop through each tree file in the folder
for (tree2_path in tree_files) {
  # Calculate and print distance metrics for the current pair of trees
  result <- calculate_tree_distances(tree1_path, tree2_path, summary_path)
  print(result)
}