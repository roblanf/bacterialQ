library(ape)
library(castor)
library(dplyr)
library(tibble)
library(tidyr)
library(stringr)
library(tidytree)
library(optparse)

# Define command-line options
option_list <- list(
  make_option(c("-t", "--tree"), type = "character", help = "Path to the Newick format tree file"),
  make_option(c("-c", "--csv"), type = "character", help = "Path to the combined_df CSV file"),
  make_option(c("-s", "--safe_taxa"), type = "character", default = NULL, help = "Path to the safe taxa list file"),
  make_option(c("-n", "--candidate_taxa"), type = "character", help = "Candidate taxa name to select the outgroup from its sister group"),
  make_option(c("-o", "--output"), type = "character", help = "Output file to print the selected taxon (species)"),
  make_option(c("-d", "--min_dist"), type = "numeric", default = 1, help = "Minimal distance with candidate taxa name to the outgroup"),
  make_option(c("-N", "--num_taxon"), type = "integer", default = 10, help = "Number of taxon (species) to select from sister group"),
  make_option(c("--detail"), action = "store_true", default = FALSE, help = "Print detailed information to a file")
)

# Parse command-line options
opt <- parse_args(OptionParser(option_list = option_list))

# Read input files
global_tree <- ape::read.tree(opt$tree)
combined_df <- read.csv(opt$csv)
safe_taxa <- if (!is.null(opt$safe_taxa)) readLines(opt$safe_taxa) else NULL

# Extract taxa information from the tree
global_treedf <- as_tibble(global_tree)
taxon_node <- global_treedf %>%
  filter(!is.na(branch.length)) %>%
  filter(node > length(global_tree$tip.label)) %>%
  filter(nzchar(label) > 0) %>%
  filter(is.na(suppressWarnings(as.numeric(label)))) %>%
  mutate(label = trimws(label, "both", "'")) %>%
  separate(label, into = c("support_value", "taxa_info"), sep = "\\|", extra = "merge") %>%
  mutate(taxa_info = strsplit(taxa_info, "/")) %>%
  unnest(taxa_info) %>%
  separate(taxa_info, into = c("rank", "taxon"), sep = "__", extra = "merge")

# Extract candidate taxa information
candidate_taxa <- strsplit(opt$candidate_taxa, "__")[[1]]
taxa_scale <- candidate_taxa[1]
taxa_name <- candidate_taxa[2]

# Function to get distances from tips to root
get_tip_dist_to_root <- function(tree) {
  n_tip <- length(tree$tip.label)
  n_node <- tree$Nnode
  distances <- get_all_distances_to_root(tree, as_edge_count = FALSE)
  return(distances[1:n_tip])
}

# Find the candidate taxa node
candidate_node <- taxon_node %>%
  filter(rank == taxa_scale, taxon == taxa_name) %>%
  pull(node)

# Calculate distances to candidate taxa node
ranked_nodes <- taxon_node %>%
  filter(rank == taxa_scale, taxon != taxa_name) %>%
  mutate(distance = sapply(node, function(n) {
    get_pairwise_distances(global_tree, n, candidate_node)
  })) %>%
  arrange(distance)

# Filter out safe taxa
if (!is.null(safe_taxa)) {
  ranked_nodes <- ranked_nodes %>%
    filter(taxon %in% safe_taxa)
  if (nrow(ranked_nodes) == 0) {
    cat("No candidate taxa found after filtering safe taxa\n")
    quit()
  }
}

# Select top 10 ranked nodes (or less if there are not enough)
ranked_nodes <- ranked_nodes %>%
  slice_head(n = 10)

# Calculate mean_tip_depth for each node
ranked_nodes <- ranked_nodes %>%
  rowwise() %>%
  mutate(mean_tip_depth = {
    subtree <- extract.clade(global_tree, node)
    mean(get_tip_dist_to_root(subtree))
  }) %>%
  ungroup()

# Re-arrange ranked_nodes based on mean_tip_depth + distance
ranked_nodes <- ranked_nodes %>%
  arrange(mean_tip_depth + distance)

# Extract subtree of the candidate taxa
candidate_taxa_tree <- extract.clade(global_tree, candidate_node)
candidate_min_depth <- min(get_tip_dist_to_root(candidate_taxa_tree))
min_dist_to_candidate_root <- opt$min_dist - candidate_min_depth

# Loop through ranked nodes to find the best outgroup
selected_tips <- NULL
outgroup_info <- NULL
for (i in 1:nrow(ranked_nodes)) {
  candidate_outgroup <- ranked_nodes[i, ]
  outgroup_tree <- extract.clade(global_tree, candidate_outgroup$node)
  if (length(outgroup_tree$tip.label) < opt$num_taxon) next
  
  outgroup_distances <- get_tip_dist_to_root(outgroup_tree) + ranked_nodes[i, ]$distance
  outgroup_df <- combined_df %>% filter(ID %in% outgroup_tree$tip.label) %>% 
    mutate(dist_to_candidate_root = outgroup_distances) %>% 
    filter(dist_to_candidate_root >= min_dist_to_candidate_root)

  if (nrow(outgroup_df) < 0.5 * length(outgroup_tree$tip.label)) next
  
  outgroup_df <- outgroup_df %>%
    rowwise() %>%
    mutate(mean_integrity = mean(c_across(matches("\\.(f|F)(a|A|n|N)[a-zA-Z]*$")), na.rm = TRUE)) %>%
    ungroup() %>% 
    arrange(desc(mean_integrity))
  
  selected_tips <- outgroup_df %>%
    slice_head(n = opt$num_taxon) %>%
    pull(ID)

  taxa_scale_fullname <- switch(taxa_scale,
                              "d" = "Domain",
                              "p" = "Phylum",
                              "c" = "Class",
                              "o" = "Order",
                              "f" = "Family",
                              "g" = "Genus",
                              "s" = "Species",
                              "Species")
                            
  outgroup_info <- outgroup_df %>%
    slice_head(n = opt$num_taxon) %>%
    mutate(min_dist_to_candidate_taxa = dist_to_candidate_root + candidate_min_depth) %>% 
    select(ID, all_of(taxa_scale_fullname), mean_integrity, min_dist_to_candidate_taxa)
    
  break
}

# Print and write selected tips to output file
if (!is.null(selected_tips)) {
  outgroup_name <- ranked_nodes[i, ]$taxon
  cat(sprintf("Select %s %s as the outgroup for %s %s\n", taxa_scale_fullname, outgroup_name, taxa_scale_fullname, taxa_name))
  writeLines(selected_tips, opt$output)
  
  if (opt$detail) {
    detail_file <- file.path(dirname(opt$output), "outgroup_species_info.txt")
    
    # Open the file connection in write mode for the first write operation
    file_conn <- file(detail_file, open = "wt")
    
    # Write the selection information
    writeLines(sprintf("Select %s %s as the outgroup for %s %s\n", taxa_scale_fullname, outgroup_name, taxa_scale_fullname, taxa_name), file_conn)
    writeLines("\nSelected Outgroup Species Information:\n", file_conn)
    
    # Close the file connection to flush the content
    close(file_conn)
    
    # Re-open the file connection in append mode for subsequent writes
    file_conn <- file(detail_file, open = "a")
    
    # Format the outgroup_info table
    outgroup_info <- outgroup_info %>%
      mutate(across(where(is.numeric), ~ round(., 3)))  # Round numeric columns to 3 decimal places
    
    # Write the formatted table, appending to the file
    write.table(outgroup_info, file_conn, row.names = FALSE, col.names = TRUE, sep = "\t", quote = FALSE, append = TRUE)
    
    # if the number of selected tips is more than 1, create the distance matrix for outgroup speceis
    if (length(selected_tips) > 1) {
      # Add a newline before the distance matrix
      writeLines("\nDistance Matrix:\n", file_conn)
      # Extract and format the distance matrix
      outgroup_subtree <- keep.tip(outgroup_tree, selected_tips)
      distance_matrix <- cophenetic(outgroup_subtree)
      distance_matrix <- round(distance_matrix, 3)  # Round the distance matrix to 3 decimal places
      
      # Write the formatted distance matrix, appending to the file
      write.table(distance_matrix, file_conn, row.names = TRUE, col.names = TRUE, sep = "\t", quote = FALSE, append = TRUE)
    }
    
    # Close the file connection
    close(file_conn)
  }
} else {
  cat(sprintf("No outgroup taxa found for %s\n", taxa_name))
}