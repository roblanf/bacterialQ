
# Example for attaching data to a tree with %<+%
library(ggtree)
info <- data.frame(taxa = phylum_tree_simple$tip.label)
info[, "type"] <- ifelse(info[["taxa"]] %in% c("p__Actinomycetota", "p__Patescibacteria", "p__Chloroflexota", "p__Cyanobacteriota", "p__Acidobacteriota", "p__Spirochaetota", "p__Gemmatimonadota"), "red", "blue")
options(repr.plot.width=15, repr.plot.height=30)
p <- ggtree(phylum_tree_simple, layout="rectangular")
p <- p %<+% info + geom_tiplab(align=FALSE, geom = "text", aes(colour = type)) + theme_tree2() +
  scale_color_manual(values = c("#377EB8", "#E41A1C"), guide='none')