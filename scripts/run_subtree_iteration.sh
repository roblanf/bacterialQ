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
#SBATCH --cpus-per-task=20  # reserve 20 cpus/threads per task
# SBATCH --ntasks-per-node=1 # only allow z tasks per node
#
# NOSBATCH --mail-user u7457359@anu.edu.au # mail user on job state changes
# SBATCH --mail-type TIME_LIMIT,FAIL		# state changes


#run the program/s and overide main resevations above for N(nodes),n(tasks) if need be
#but make sure the overides add up to no more than the totals in your SBATCH resevatons if used
#see https://supercomputing.swin.edu.au/docs/2-ozstar/oz-slurm-examples.html#packed-jobs-example
# https://rc-docs.northeastern.edu/en/latest/using-discovery/sbatch.html#sbatch-examples

conda init bash
source /opt/conda/bin/activate /home/u7457359/.conda/envs/qgtdb
cd /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/scripts

tree_file="/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/r207_original_clean.tree"
train_loc_path="/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/alignment/train"
test_loc_path="/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/alignment/test"
model_dir="/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/modelset_ALL.nex"
RESULT_DIR="../Result"
combined_table="/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/combined_df.csv"

taxa_name="p__Desulfobacterota"
select_size=20

srun python subtree_model_iteration.py --taxa_scale phylum\
                                  --taxa_name $taxa_name\
                                  --select_size $select_size\
                                  --train_loc_path $train_loc_path \
                                  --test_loc_path $test_loc_path \
                                  --taxa_file $combined_table\
                                  --ref_tree $tree_file \
                                  --model_dir $model_dir \
                                  --output_dir $RESULT_DIR \
                                  --max_threads 20
 