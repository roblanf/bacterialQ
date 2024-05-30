# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(stringr)

# Read the data
iqtree_summary <- read.csv("/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/scripts/TESTING/sum_res/combined_iqtree_sum.csv")

# Extract 'phylum' and 'max_tree_size' from 'result_name'
iqtree_summary <- iqtree_summary %>%
  mutate(
    phylum = str_replace(result_name, ".*_(\\d+_\\d+)$", "\\1"),
    max_tree_size = as.numeric(str_extract(result_name, "\\d+"))
  ) %>% 
  filter(!is.na(as.numeric(loop))) %>% 
  mutate(cpu_time = cpu_time / 3600)

# Create a scatter plot of 'max_tree_size' and 'cpu_time', facet by 'loop' and 'step'
p <- ggplot(iqtree_summary, aes(x = max_tree_size, y = cpu_time)) +
  geom_point() +
  facet_grid(loop ~ step) +
  theme_gray()

# Save the plot to the current directory
ggsave("scatter_plot.png", plot = p)