import subprocess
import os
from quality_trimming import generate_combined_df

train_loc_path = "/home/tim/project/GTDB_TREE/alignment/r220/train"
test_loc_path = "/home/tim/project/GTDB_TREE/alignment/r220/test"
taxa_file = "/home/tim/project/GTDB_TREE/data/r220/rep_bac120_taxonomy.tsv"
output_dir = "../data/r220"

# for test
# train_loc_path = "/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/p__Actinobacteriota_200/p__Actinobacteriota_200_002/loci/training_loci"
# test_loc_path = "/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/Result/p__Actinobacteriota_200/p__Actinobacteriota_200_002/loci/testing_loci"

generate_combined_df(train_loc_path, test_loc_path, taxa_file, output_dir)
