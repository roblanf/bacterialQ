# Load necessary libraries
library(ape)
library(castor)

#' Function reads a phylogenetic tree , finds the nearest tips for each tip, and calculates their branch length.
#' @param tree_file A string representing the file path to the Newick file containing the phylogenetic tree.
#' @return A data frame with columns 'tip1', 'tip2', and 'branch_length', representing the nearest tip pairs and the branch lengths between them.
tree_to_near_tips <- function(tree_file) {
    # Read the tree from the Newick file
    tree <- read.tree(tree_file)

    # Find the nearest tips for each tip
    nearest_tips <- get_all_pairwise_distances(tree, only_clades = 1:length(tree$tip.label))

    find_min_indices <- function(mat) {
        n <- nrow(mat)
        min_indices <- integer(n)

        for (i in 1:n) {
            row <- mat[i, ]
            row[i] <- Inf
            min_indices[i] <- which.min(row)
        }
        return(min_indices)
    }
    min_indices <- find_min_indices(nearest_tips)
    # Create a data frame with tip1 and tip2
    tip_pairs <- data.frame(tip1 = tree$tip.label, tip2 = tree$tip.label[min_indices], branch_length = nearest_tips[cbind(1:length(tree$tip.label), min_indices)])

    return(tip_pairs)
}

library(dplyr)
library(tidyr)
library(ggplot2)
# Function to perform permutation test and generate a density plot
# @description Perform a permutation test to compare the mean branch lengths between two tips and generate a density plot
# @param tree_table Data frame containing the tree structure with columns tip1, tip2, and branch_length
# @param dist_table Data frame containing the distance information with dynamic column names
# @param tip1 Column name in dist_table for the first tip
# @param tip2 Column name in dist_table for the second tip
# @param value Column name in dist_table for the distance value
# @param n_permutations Number of permutations to perform
# @param side Type of test: "both", "greater", or "less"
# @return A list containing the p-value of the permutation test and the ggplot format density plot
near_tips_permutation_test <- function(tree_table, dist_table, tip1, tip2, value, n_permutations = 10000, side = "both") {
    # Extract all unique tips
    tips <- unique(c(dist_table[[tip1]], dist_table[[tip2]]))

    # Function to calculate mean branch length for a given tree_table
    calculate_mean_branch_length <- function(tree_table, dist_table, tip1, tip2, value) {
        tree_table %>%
            left_join(dist_table, by = c("tip1" = tip1, "tip2" = tip2)) %>%
            summarise(mean_value = mean(.data[[value]], na.rm = TRUE)) %>%
            pull(mean_value)
    }

    # Calculate the observed mean branch length
    observed_mean <- calculate_mean_branch_length(tree_table, dist_table, tip1, tip2, value)

    # Perform permutations
    permuted_means <- replicate(n_permutations, {
        # Create a deep copy of the tree_table
        permuted_tree <- tree_table

        # Shuffle the tips
        shuffled_tips <- sample(tips)
        tip_mapping <- setNames(shuffled_tips, tips)

        # Remap the tips in the tree_table
        permuted_tree <- permuted_tree %>%
            mutate(
                tip1 = tip_mapping[tip1],
                tip2 = tip_mapping[tip2]
            )

        # Calculate the mean branch length for the permuted tree
        calculate_mean_branch_length(permuted_tree, dist_table, tip1, tip2, value)
    })

    # Calculate the p-value based on the side of the test
    if (side == "both") {
        p_value <- mean(abs(permuted_means) >= abs(observed_mean))
    } else if (side == "greater") {
        p_value <- mean(permuted_means >= observed_mean)
    } else if (side == "less") {
        p_value <- mean(permuted_means <= observed_mean)
    } else {
        stop("Invalid value for 'side'. Choose from 'both', 'greater', or 'less'.")
    }
    if (observed_mean > median(permuted_means)) {
        hjust <- 1
    } else {
        hjust <- 0
    }
    # Create the density plot
    plot <- ggplot(data.frame(permuted_means = permuted_means), aes(x = permuted_means)) +
        geom_density(fill = "blue", alpha = 0.5) +
        geom_vline(xintercept = observed_mean, color = "red", linetype = "dashed") +
        annotate("text",
            x = observed_mean, y = max(density(permuted_means)$y), hjust = hjust,
            label = paste("Observed Mean:", round(observed_mean, 2)),
            vjust = -1, color = "red"
        ) +
        annotate("text",
            x = observed_mean, y = max(density(permuted_means)$y) * 0.9,
            label = paste("Side:", side, "\nP-value:", round(p_value, 4)), hjust = hjust,
            vjust = -0.75, color = "black"
        ) +
        labs(title = "Permutation Test Density Plot", x = str_c("Permuted Mean (n=", n_permutations, ")"), y = "Density")

    # Return the p-value and the plot separately
    return(list(p_value = p_value, plot = plot))
}
