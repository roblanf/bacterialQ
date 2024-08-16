#!/bin/bash

python subtree_model_iteration.py \
--taxa_scale phylum \
--taxa_name p__Acidobacteriota \
--num_aln 188 \
--loci_path /home/tim/project/bacterialQ/alignment/r220/combined \
--taxa_file /home/tim/project/bacterialQ/data/r220/combined_df.csv \
--ref_tree /home/tim/project/bacterialQ/data/r220/bac120_r220.tree \
--model_dir /home/tim/project/bacterialQ/data/modelset_ALL.nex \
--output_dir ../Result_nova/test \
--FastTreeMP_path /home/tim/tool/FastTreeMP/FastTreeMP \
--max_threads 50 \
--tree_size_lower_lim 10 \
--tree_size_upper_lim 50 \
--prune_mode split \
--use_outgroup \
--decorated_tree /home/tim/project/bacterialQ/data/r220/bac120_r220_decorated.tree \
--outgroup_taxa_list /home/tim/project/bacterialQ/data/GTDB_stable_phyla_list.txt \
--time_limit 86400 \
--verbose \
--estimate_best_final_tree \
--test_final_tree \
--final_tree_tool IQFAST \
--model_update_summary \
--tree_comparison_report \
--fix_subtree_topology
