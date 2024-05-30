#!/bin/bash

#Typical settings one can use, although not all at the same time.
#Be fair to others and leave some excess capacity for other jobs
#
# SBATCH --job-name=Q.GTDB_subtree_test
# SBATCH --output=/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/OUTPUTS/OUTPUT.out
# SBATCH --error=/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/OUTPUTS/ERROR.err
# SBATCH --partition=Standard
#
#SBATCH --time=120:00:00    # 5 days then stop job if not complete
#SBATCH --mem-per-cpu=7000  # 7GB per cpu (rather than per node)
#SBATCH --nodes=1	    # use 1 nodes
#SBATCH --cpus-per-task=60  # reserve 40 cpus/threads per task
# SBATCH --ntasks-per-node=1 # only allow z tasks per node
#
# NOSBATCH --mail-user u7457359@anu.edu.au # mail user on job state changes
# SBATCH --mail-type TIME_LIMIT,FAIL		# state changes


#run the program/s and overide main resevations above for N(nodes),n(tasks) if need be
#but make sure the overides add up to no more than the totals in your SBATCH resevatons if used
#see https://supercomputing.swin.edu.au/docs/2-ozstar/oz-slurm-examples.html#packed-jobs-example
# https://rc-docs.northeastern.edu/en/latest/using-discovery/sbatch.html#sbatch-examples

tree_file="/home/tim/project/GTDB_TREE/data/r207_original_clean.tree"
train_loc_path="/home/tim/project/GTDB_TREE/alignment/train"
test_loc_path="/home/tim/project/GTDB_TREE/alignment/test"
model_dir="/home/tim/project/GTDB_TREE/data/modelset_ALL.nex"
RESULT_DIR="../Result_rona"
combined_table="/home/tim/project/GTDB_TREE/Result/combined_df.csv"
FastTreeMP_path="/home/tim/project/tool/FastTreeMP/FastTreeMP"

taxa_name="p__Bipolaricaulota"
num_aln=50

python subtree_model_iteration.py --taxa_scale phylum\
                                  --taxa_name $taxa_name\
                                  --num_aln $num_aln\
                                  --train_loc_path $train_loc_path \
                                  --test_loc_path $test_loc_path \
                                  --taxa_file $combined_table\
                                  --ref_tree $tree_file \
                                  --model_dir $model_dir \
                                  --output_dir $RESULT_DIR \
                                  --FastTreeMP_path $FastTreeMP_path \
                                  --max_threads AUTO \
                                  --tree_size_lower_lim 10 \
                                  --tree_size_upper_lim 15 \
                                  --prune_mode upper \
                                  --verbose \
                                  --test_in_loop 

 