# Load required libraries
library(ape)
library(phangorn)
library(ggplot2)

# Define a function to extract the tree name from the file path
extract_tree_name <- function(file_path) {
    # Remove the directory path and file extension from the file path
    tree_name <- sub("^.*\\/", "", file_path)
    tree_name <- sub("\\..*$", "", tree_name)
    return(tree_name)
}

# Define a function to calculate distance metrics between two trees
calculate_tree_distances <- function(tree1_file, tree2_file, dir_path) {
    # Read tree files
    tree1 <- read.tree(paste0(dir_path, "/", tree1_file))
    tree2 <- read.tree(paste0(dir_path, "/", tree2_file))


    ifroot <- is.rooted(tree1) && is.rooted(tree2)

    if (!ifroot) {
        tree1 <- unroot(tree1)
        tree2 <- unroot(tree2)
    }

    # Check if the taxa of the two trees are equal
    taxa_equal <- setequal(tree1$tip.label, tree2$tip.label)
    if (!taxa_equal) {
        taxa_diff1 <- setdiff(tree1$tip.label, tree2$tip.label)
        taxa_diff2 <- setdiff(tree2$tip.label, tree1$tip.label)
        cat("The taxa of the two trees are not equal.\n")
        cat("Number of taxa unique to Tree 1:", length(taxa_diff1), "\n")
        cat("Number of taxa unique to Tree 2:", length(taxa_diff2), "\n")
        cat("The differing taxa have been removed for the analysis.\n")
        tree1 <- drop.tip(tree1, taxa_diff1)
        tree2 <- drop.tip(tree2, taxa_diff2)
    }

    # Extract tree names from file paths
    tree1_name <- extract_tree_name(tree1_file)
    tree2_name <- extract_tree_name(tree2_file)

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

    # Define the summary file path
    summary_path <- paste0(dir_path, "/../tree_pairwise_compare.csv")

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

# Define a function to generate heatmaps
generate_heatmaps <- function(dir_path) {
    # Define the summary file path
    summary_path <- paste0(dir_path, "/../tree_pairwise_compare.csv")

    # Read the summary file
    summary_df <- read.csv(summary_path)

    # Generate heatmaps
    RF_heatmap <- ggplot(summary_df, aes(x = Tree1, y = Tree2, fill = RF_dist)) +
        geom_tile() +
        theme_minimal() +
        labs(title = "RF Distance of Trees")
    ggsave(paste0(dir_path, "/../RF_dist.png"), RF_heatmap, width = 8, height = 6)

    nRF_heatmap <- ggplot(summary_df, aes(x = Tree1, y = Tree2, fill = nRF)) +
        geom_tile() +
        theme_minimal() +
        labs(title = "nRF Distance of Trees")
    ggsave(paste0(dir_path, "/../nRF_dist.png"), nRF_heatmap, width = 8, height = 6)
}

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 1) {
    stop("Usage: Rscript script.R <dir_path>")
}

# Assign command line argument to variable
dir_path <- args[1]

# Get all tree files in the directory
tree_files <- list.files(dir_path)
tree_files <- tree_files[grepl("\\..*tre.*$", tree_files)]

# Get all possible pairs of tree files
tree_pairs <- combn(tree_files, 2)

# Calculate distances for all pairs of tree files
for (i in seq(ncol(tree_pairs))) {
    calculate_tree_distances(tree_pairs[1, i], tree_pairs[2, i], dir_path)
}

# Generate heatmaps
# generate_heatmaps(dir_path)
