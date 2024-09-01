#!/bin/bash

python subtree_model_iteration.py \
--taxa_scale phylum \
--taxa_name p__Krumholzibacteriota \
--num_aln 2000 \
--loci_path /home/tim/project/bacterialQ/alignment/r220/combined \
--taxa_file /home/tim/project/bacterialQ/data/r220/combined_df.csv \
--ref_tree /home/tim/project/bacterialQ/data/r220/bac120_r220.tree \
--model_dir /home/tim/project/bacterialQ/data/modelset_ALL.nex \
--output_dir ../Result_nova/phylum_models \
--FastTreeMP_path /home/tim/tool/FastTreeMP/FastTreeMP \
--max_threads 50 \
--tree_size_lower_lim 15 \
--tree_size_upper_lim 93 \
--prune_mode split \
--use_outgroup \
--decorated_tree /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree \
--outgroup_taxa_list /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt \
--max_iterate 4 \
--verbose \
--test_final_tree \
--final_tree_tool FT \
--model_update_summary \
--tree_comparison_report \
--fix_subtree_topology \
--keep_aln
