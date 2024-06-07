#!/bin/bash

#Typical settings one can use, although not all at the same time.
#Be fair to others and leave some excess capacity for other jobs
#
#SBATCH --job-name=Q.GTDB_subtree_test
# SBATCH --output=/home/tim/project/GTDB_TREE/scriptsResult/OUTPUTS/OUTPUT.out
# SBATCH --error=/home/tim/project/GTDB_TREE/scriptsResult/OUTPUTS/ERROR.err
#SBATCH --partition=Standard
#
#SBATCH --time=120:00:00    # 5 days then stop job if not complete
#SBATCH --mem-per-cpu=7000  # 7GB per cpu (rather than per node)
#SBATCH --nodes=1	    # use 1 nodes
#SBATCH --cpus-per-task=40  # reserve 40 cpus/threads per task
#SBATCH --ntasks-per-node=1 # only allow z tasks per node
#
# NOSBATCH --mail-user u7457359@anu.edu.au # mail user on job state changes
#SBATCH --mail-type TIME_LIMIT,FAIL		# state changes


#run the program/s and overide main resevations above for N(nodes),n(tasks) if need be
#but make sure the overides add up to no more than the totals in your SBATCH resevatons if used
#see https://supercomputing.swin.edu.au/docs/2-ozstar/oz-slurm-examples.html#packed-jobs-example
# https://rc-docs.northeastern.edu/en/latest/using-discovery/sbatch.html#sbatch-examples

tree_file="/home/tim/project/GTDB_TREE/data/r220/bac120_r220.tree"
train_loc_path="/home/tim/project/GTDB_TREE/alignment/r220/train"
test_loc_path="/home/tim/project/GTDB_TREE/alignment/r220/test"
model_dir="/home/tim/project/GTDB_TREE/data/modelset_ALL.nex"
RESULT_DIR="../Result_rona"
combined_table="/home/tim/project/GTDB_TREE/data/r220/combined_df.csv"
FastTreeMP_path="/home/tim/project/tool/FastTreeMP/FastTreeMP"

taxa_name="p__Acidobacteriota"
num_aln=1000

python subtree_model_iteration.py --taxa_scale phylum\
                                  --taxa_name $taxa_name\
                                  --num_aln $num_aln\
                                  --train_loc_path $train_loc_path \
                                  --test_loc_path $test_loc_path \
                                  --taxa_file $combined_table\
                                  --ref_tree $tree_file \
                                  --model_dir $model_dir \
                                  --output_dir ${RESULT_DIR}/test \
                                  --FastTreeMP_path $FastTreeMP_path \
                                  --max_threads 50 \
                                  --tree_size_lower_lim 5 \
                                  --tree_size_upper_lim 66 \
                                  --prune_mode random \
                                  --verbose \
                                  --test_in_loop \
                                  --test_partition


# srun iqtree -T 20 -S /home/tim/project/GTDB_TREE/scriptsResult/p__Desulfobacterota_300/loop_1/loci/testing_loci -m MFP -mset LG,p__Desulfobacterota_300_1,Q.INSECT,p__Desulfobacterota_300_3,Q.PFAM,Q.YEAST,p__Desulfobacterota_300_2,p__Desulfobacterota_300_4 -mdef /home/tim/project/GTDB_TREE/scriptsResult/p__Desulfobacterota_300/trained_models/trained_model.nex  -pre /home/tim/project/GTDB_TREE/scriptsResult/p__Desulfobacterota_300/final_verification/p__Desulfobacterota_300_verify_
