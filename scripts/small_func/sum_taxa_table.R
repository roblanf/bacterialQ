# Load required libraries
library(dplyr)
library(ggplot2)

# Read CSV file into a tibble
df <- read.csv("/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/combined_df.csv", stringsAsFactors = FALSE) %>%
    as_tibble()

# Calculate mean, median, and 25th quantile of integrity values
df <- df %>%
    rowwise() %>%
    mutate(
        mean_integrity = mean(c_across(where(is.numeric)), na.rm = TRUE),
        median_integrity = median(c_across(where(is.numeric)), na.rm = TRUE),
        q25_integrity = quantile(c_across(where(is.numeric)), probs = 0.25, na.rm = TRUE)
    ) %>%
    ungroup()

# Summarize data by phylum, sort by descending number of species
phylum_summary <- df %>%
    group_by(Phylum) %>%
    summarise(
        n_species = n(),
        n_classes = n_distinct(Class),
        mean_integrity = mean(mean_integrity, na.rm = TRUE),
        .groups = "drop"
    ) %>%
    arrange(desc(n_species)) %>%
    filter(n_species > 10) # Filter out phyla with fewer than 10 species

# Create output directory
output_dir <- "/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/scripts/small_func/output"
dir.create(output_dir, recursive = TRUE)

# Save phylum summary as CSV
write.csv(phylum_summary, file.path(output_dir, "phylum_summary.csv"), row.names = FALSE)

# Plot number of species by phylum
p1 <- ggplot(phylum_summary, aes(x = reorder(Phylum, n_species), y = n_species)) +
    geom_col() +
    xlab("Phylum") +
    ylab("Number of species") +
    ggtitle("Number of species by phylum") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    scale_y_log10(breaks = c(50, 100, 200)) + # Log10 scale with custom breaks
    geom_hline(yintercept = c(50, 100, 200), linetype = "dashed") # Add horizontal dashed lines

# Save species by phylum plot
ggsave(file.path(output_dir, "species_by_phylum.png"), p1, width = 8, height = 6, dpi = 300)

# Summarize data by phylum and class
class_by_phylum <- df %>%
    group_by(Phylum, Class) %>%
    summarise(n_species = n()) %>%
    ungroup()

# Plot number of species by phylum and class
p2 <- ggplot(class_by_phylum, aes(x = Phylum, y = n_species, fill = Class)) +
    geom_col() +
    xlab("Phylum") +
    ylab("Number of species") +
    ggtitle("Number of species by phylum and class") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "none") # Hide legend

# Save species by phylum and class plot
ggsave(file.path(output_dir, "species_by_phylum_class.png"), p2, width = 8, height = 6, dpi = 300)
