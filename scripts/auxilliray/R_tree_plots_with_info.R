# Example for attaching data to a tree with %<+%
library(ggtree)
info <- data.frame(taxa = phylum_tree_simple$tip.label)
info[, "type"] <- ifelse(info[["taxa"]] %in% c("p__Actinomycetota", "p__Patescibacteria", "p__Chloroflexota", "p__Cyanobacteriota", "p__Acidobacteriota", "p__Spirochaetota", "p__Gemmatimonadota"), "red", "blue")
options(repr.plot.width = 15, repr.plot.height = 30)
p <- ggtree(phylum_tree_simple, layout = "rectangular")
p <- p %<+% info + geom_tiplab(align = FALSE, geom = "text", aes(colour = type)) + theme_tree2() +
  scale_color_manual(values = c("#377EB8", "#E41A1C"), guide = "none")



library(ggtree)
library(ape)
library(tidyverse)

safe_phyla <- c("p__Chlamydiota", "p__Marinisomatota", "p__Deinococcota", "p__Synergistota", "p__Fibrobacterota", "p__Margulisbacteria", "p__Cloacimonadota", "p__Fusobacteriota", "p__Zixibacteria", "p__Aquificota", "p__Dependentiae", "p__Thermotogota", "p__Bipolaricaulota", "p__Poribacteria", "p__Krumholzibacteriota", "p__Eisenbacteria", "p__Deferribacterota", "p__Caldisericota")
large_phyla <- c("p__Actinomycetota", "p__Patescibacteria", "p__Chloroflexota", "p__Cyanobacteriota", "p__Acidobacteriota", "p__Spirochaetota", "p__Gemmatimonadota")

df <- read.csv("/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/r220/rep_bac120_taxonomy.tsv", stringsAsFactors = FALSE, sep = "\t") %>%
  as_tibble()

info <- df %>%
  group_by(Phylum) %>%
  summarise(
    n_species = n(),
    n_classes = n_distinct(Class),
    .groups = "drop"
  ) %>%
  arrange(desc(n_species)) %>%
  filter(n_species > 10) %>%
  rename(taxa = Phylum)

info <- info %>%
  mutate(type = case_when(
    taxa %in% safe_phyla ~ "blue",
    taxa %in% large_phyla ~ "red",
    TRUE ~ "black"
  ))

phylum_tree_simple <- read.tree("/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/analysis/phylum_tree/phylum_backbone_simple.tre")
phylum_tree_simple <- keep.tip(phylum_tree_simple, info$taxa)

options(repr.plot.width = 15, repr.plot.height = 30)

p <- ggtree(phylum_tree_simple, layout = "rectangular")

p <- p %<+% info +
  geom_tiplab(align = FALSE, geom = "text", aes(colour = type)) +
  geom_point(aes(size = n_species, alpha = 0.5), shape = 21, fill = "white") +
  theme_tree2() +
  scale_color_manual(values = c("blue" = "#377EB8", "red" = "#E41A1C", "black" = "#000000"), guide = "none") +
  scale_size_continuous(range = c(0, 10), trans = "sqrt", breaks = c(200, 1000, 2500, 5000, 10000, 20000)) +
  scale_alpha_continuous(range = c(0.5, 0.5), guide = "none")


print(p)
