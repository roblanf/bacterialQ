#!/bin/sh  
#Typical settings one can use, although not all at the same time.
#Be fair to others and leave some excess capacity for other jobs
#
#SBATCH --job-name=Q.GTDB_Spirochaetota
#SBATCH --output=/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/slurm_log/OUTPUT.out
#SBATCH --error=/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/slurm_log/ERROR.err
#SBATCH --partition=Standard
#
#SBATCH --time=120:00:00    # 5 days then stop job if not complete
#SBATCH --mem-per-cpu=7000  # 7GB per cpu (rather than per node)
#SBATCH --nodes=1	    # use 1 nodes
#SBATCH --cpus-per-task=50  # reserve 40 cpus/threads per task
#SBATCH --ntasks-per-node=1 # only allow z tasks per node
#
#SBATCH --mail-user u7457359@anu.edu.au # mail user on job state changes
#SBATCH --mail-type TIME_LIMIT,FAIL		# state changes

srun python additional_cross_test.py /mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/safe_phyla