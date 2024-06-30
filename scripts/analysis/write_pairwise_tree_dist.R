library(ape)
library(phangorn)
library(ggplot2)
library(ggplot2)
library(dplyr)
library(tidyr)
library(tibble)
library(vegan)
library(ggrepel)
library(dendextend)

# Define a function to extract the tree name from the file path
extract_tree_name <- function(file_path) {
    # Remove the directory path and file extension from the file path
    tree_name <- sub("^.*\\/", "", file_path)
    tree_name <- sub("\\..*$", "", tree_name)
    return(tree_name)
}

# Define a function to calculate distance metrics between two trees
calculate_tree_distances <- function(tree1_file, tree2_file, dir_path) {
    # Ensure tree1_file is lexicographically larger than tree2_file
    if (tree1_file < tree2_file) {
        temp <- tree1_file
        tree1_file <- tree2_file
        tree2_file <- temp
    }

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
    summary_path <- paste0(dir_path, "/tree_pairwise_compare.csv")

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

#' @description Generate a heatmap from a CSV file with hierarchical clustering
#' @param csv_path Path to the CSV file
#' @param value_col Column name for the values to be clustered
#' @param output_path Path to save the output heatmap
#' @param cluster_col1 Column name for the first tree
#' @param cluster_col2 Column name for the second tree
generate_heatmap <- function(csv_path, value_col, output_path, cluster_col1 = "Tree1", cluster_col2 = "Tree2") {
    # Read the CSV file
    summary_df <- read.csv(csv_path)

    # Create a symmetric dataframe
    summary_df_sym <- summary_df %>%
        rename(!!sym(cluster_col1) := !!sym(cluster_col2), !!sym(cluster_col2) := !!sym(cluster_col1))
    summary_df <- rbind(summary_df, summary_df_sym)

    # Create the distance matrix
    dist_matrix <- summary_df %>%
        select(!!sym(cluster_col1), !!sym(cluster_col2), !!sym(value_col)) %>%
        spread(!!sym(cluster_col2), !!sym(value_col)) %>%
        column_to_rownames(var = cluster_col1) %>%
        as.matrix()

    dist_matrix[is.na(dist_matrix)] <- 0 # Replace NA values with 0

    # Perform hierarchical clustering
    hc <- hclust(as.dist(dist_matrix), method = "complete")

    # Create a dendrogram
    dend <- as.dendrogram(hc)

    # Generate heatmap with clustering
    summary_df <- summary_df %>%
        mutate(
            !!sym(cluster_col1) := factor(!!sym(cluster_col1), levels = hc$labels[hc$order]),
            !!sym(cluster_col2) := factor(!!sym(cluster_col2), levels = hc$labels[hc$order])
        )

    # Filter to only lower triangle
    summary_df <- summary_df %>%
        filter(as.numeric(!!sym(cluster_col1)) >= as.numeric(!!sym(cluster_col2)))

    # Generate heatmap
    heatmap <- ggplot(summary_df, aes_string(x = cluster_col1, y = cluster_col2, fill = value_col)) +
        geom_tile() +
        geom_text(aes_string(label = value_col), size = 3) + # Add text annotations
        coord_equal() +
        scale_fill_gradient(low = "white", high = "red") +
        labs(x = cluster_col1, y = cluster_col2, fill = value_col) +
        theme_light() +
        theme(
            axis.text = element_text(size = 10),
            panel.background = element_rect(fill = "white"),
            panel.grid.major = element_blank(), # Remove major grid lines
            panel.grid.minor = element_blank(),
            axis.text.x = element_text(angle = 45, hjust = 1)
        ) +
        scale_x_discrete(limits = hc$labels[hc$order]) + # Reorder x-axis
        scale_y_discrete(limits = hc$labels[hc$order]) # Reorder y-axis

    num_x_labels <- length(hc$labels)
    # Calculate the width of the heatmap based on the number of x-axis labels
    fig_size <- max(6, num_x_labels / 1.5)
    # Save the heatmap
    ggsave(output_path, heatmap, width = fig_size, height = fig_size)
}

# Define a function to generate heatmaps
generate_heatmaps <- function(dir_path) {
    # Define the summary file path
    summary_path <- paste0(dir_path, "/tree_pairwise_compare.csv")

    # Generate heatmaps with hierarchical clustering
    generate_heatmap(summary_path, "RF_dist", paste0(dir_path, "/RF_dist.png"))
    generate_heatmap(summary_path, "nRF", paste0(dir_path, "/nRF_dist.png"))
}

# Define a function to generate NMDS plots
plot_NMDS <- function(csv_file, metric_column, output_path) {
    # Read the summary file
    summary_df <- read.csv(csv_file)

    # Prepare data for NMDS
    summary_df_2 <- summary_df %>%
        rename(Tree2 = Tree1, Tree1 = Tree2)

    summary_df <- rbind(summary_df, summary_df_2)

    nRF_matrix <- summary_df %>%
        select(Tree1, Tree2, !!sym(metric_column)) %>%
        spread(Tree2, !!sym(metric_column))

    namerow <- nRF_matrix %>% pull(Tree1)
    nRF_matrix <- nRF_matrix %>%
        select(-Tree1) %>%
        as.matrix()
    rownames(nRF_matrix) <- namerow
    # nRF_matrix[is.nan(nRF_matrix)] <- 0

    # Perform NMDS
    z <- metaMDS(
        comm = nRF_matrix,
        autotransform = FALSE,
        distance = "euclidean",
        engine = "monoMDS",
        k = 2,
        weakties = TRUE,
        model = "global",
        maxit = 300,
        try = 50,
        trymax = 100
    )

    # Prepare data for plot
    z.points <- data.frame(z$points)

    # Create the plot
    p <- ggplot(data = z.points, aes(x = MDS1, y = MDS2, label = rownames(nRF_matrix))) +
        geom_point() +
        coord_equal() +
        theme_bw() +
        theme(
            axis.text.x = element_blank(), # remove x-axis text
            axis.text.y = element_blank()
        ) + # remove y-axis text
        geom_text_repel(max.overlaps = Inf, size = 3)

    # Save the plot
    ggsave(filename = paste0(output_path, "/NMDS_", metric_column, ".png"), plot = p)
}

# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 1) {
    stop("Usage: Rscript script.R <dir_path>")
}

# Assign command line argument to variables
dir_path <- args[1]

# Get all tree files in the directory
tree_files <- list.files(dir_path)
tree_files <- tree_files[grepl("\\..*tre.*$", tree_files, ignore.case = TRUE)]

# Get all possible pairs of tree files
tree_pairs <- combn(tree_files, 2)

# Calculate distances for all pairs of tree files
for (i in seq(ncol(tree_pairs))) {
    calculate_tree_distances(tree_pairs[1, i], tree_pairs[2, i], dir_path)
}

# Generate heatmaps
generate_heatmaps(dir_path)

# Generate NMDS plot
summary_path <- paste0(dir_path, "/tree_pairwise_compare.csv")
plot_NMDS(summary_path, "nRF", dir_path)
