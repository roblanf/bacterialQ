import sys
import os
import shutil
import subprocess
from glob import glob
from pathlib import Path
import argparse

# Get the current working directory
current_dir = os.getcwd()

# Construct the path to the module
module_path = os.path.abspath(os.path.join(current_dir, '../small_func'))

# Add the module path to sys.path if it's not already there
if module_path not in sys.path:
    sys.path.append(module_path)

try:
    from sample_alignment import sample_alignment
except ImportError as e:
    print(f"Error importing function: {e}")

def extract_taxa_name(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            if line.startswith("Taxa name:"):
                return line.split(":")[1].strip()

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def run_sample_alignment(loci_dir, taxa_list, output_folder, loci_filter):
    sample_alignment(Path(loci_dir), Path(taxa_list), Path(output_folder), num_aln=None, combine_subtree=False)

def run_concat_seq(input_dir, output_file):
    subprocess.run(["python", "../concat_seq.py", input_dir, output_file, "true"])

def run_iqtree(input_file, model_file, tree_file, output_prefix, last_model):
    # Construct the model set string
    model_set = f"LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART,{last_model}"
    # Run the iqtree command with the dynamically constructed model set
    subprocess.run([
        "iqtree", "-T", "50", "-s", input_file, "-m", "TESTONLY", 
        "-mset", model_set, "-mdef", model_file, "-te", tree_file, "-pre", output_prefix
    ])

def extract_last_treefile(directory, destination):
    loop_dirs = sorted(glob(os.path.join(directory, 'loop_*')))
    last_loop_dir = loop_dirs[-1]
    treefile = glob(os.path.join(last_loop_dir, 'tree_update', '*.treefile'))[0]
    shutil.copy(treefile, destination)

def extract_last_model(log_file_path):
    with open(log_file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines) - 1, -1, -1):
            if "Best models for test data:" in lines[i]:
                return lines[i + 1].strip()

def main(base_dir, extra_param):
    for sub_dir in os.listdir(base_dir):
        test_dir = os.path.join(base_dir, sub_dir)
        if os.path.isdir(test_dir):
            log_file_path = os.path.join(test_dir, "log.md")
            taxa_name = extract_taxa_name(log_file_path)
            
            cross_test_dir = os.path.join(test_dir, "cross_test")
            create_directory(cross_test_dir)
            
            loci_dir_train = "../../alignment/r220/train"
            loci_dir_test = "../../alignment/r220/test"
            taxa_list = os.path.join(test_dir, "select_id.txt")
            loci_filter = os.path.join(test_dir, "select_loci.txt")
            output_folder = os.path.join(cross_test_dir, "loci")
            
            run_sample_alignment(loci_dir_train, taxa_list, output_folder, loci_filter)
            run_sample_alignment(loci_dir_test, taxa_list, output_folder, loci_filter)
            
            concat_output_file = os.path.join(cross_test_dir, "concat_all.faa")
            run_concat_seq(cross_test_dir, concat_output_file)
            
            model_file = os.path.join(test_dir, "trained_models", "trained_model.nex")
            ref_tree_file = os.path.join(test_dir, "ref_tree.tre")
            concat_reftree_prefix = os.path.join(cross_test_dir, "concat_reftree")
            run_iqtree(concat_output_file, model_file, ref_tree_file, concat_reftree_prefix, last_model="")
            
            last_tree_file = os.path.join(cross_test_dir, "last_tree.treefile")
            extract_last_treefile(test_dir, last_tree_file)
            
            last_model = extract_last_model(log_file_path)
            concat_newtree_prefix = os.path.join(cross_test_dir, "concat_newtree")
            run_iqtree(concat_output_file, model_file, last_tree_file, concat_newtree_prefix, last_model)
            
            # Cleanup: delete the output_folder and concat_output_file
            shutil.rmtree(output_folder)
            os.remove(concat_output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the script with an extra parameter.")
    parser.add_argument("base_dir", type=str, help="The base directory to process.")
    parser.add_argument("extra_param", type=str, help="An extra parameter for the script.")
    args = parser.parse_args()
    
    main(args.base_dir, args.extra_param)
