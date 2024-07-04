#!/usr/bin/env python3
import argparse
import subprocess
import time
import math
import os
import sys
import shutil
import itertools
import random
from pathlib import Path
from typing import Tuple
 
# Import functional scripts
from Q_convert import *
from grep_iqtree_output import *
from quality_trimming import *
from concat_seq import concatenate_seq_dict, concatenate_seq_list
from get_subtree import prune_tree, remove_redundant_nodes
from mdlogger import *
from fasta_filter import drop_rubbish_aln

# Define constants
keep_model_thres = 0.05

def log_and_handle_error(func):
    """
    Decorator to log and handle errors in functions.
    """
    def wrapper(*args, **kwargs):
        try:
            log_message('process', f"Running {func.__name__}...")
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Log the error and re-raise the exception
            log_message('error', f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

def run_command(cmd: str, log_file: str, log_any: bool = True, log_output: bool = False, log_time: bool = False) -> Tuple[str, str, int]:
    """
    Run a shell command, log its output, and return its output and exit code.

    Args:
        cmd (str): Command to run.
        log_file (str): Path to the log file.
        log_any (bool): Whether to log the command itself.
        log_output (bool): Whether to log the command output.
        log_time (bool): Whether to log the command runtime.

    Returns:
        Tuple[str, str, int]: A tuple containing the command output (stdout), error output (stderr), and exit code.
    """
    if log_any:
        log_message('command', f"```bash\n{cmd}\n```\n")

    start_time = time.time()
    process = subprocess.Popen(cmd, shell=True, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_code = process.returncode
    end_time = time.time()
    run_time = end_time - start_time

    if log_any:
        with open(log_file, 'a') as f:
            if stderr and exit_code != 0:
                f.write(f"  Error:\n{stderr}  \n")
            if log_output and stdout:
                # Sometimes it's annoying some output was interpreted as error(e.g. Rscript)
                if stderr and exit_code == 0:
                    f.write(f"  Output:\n{stderr}  \n{stdout}  \n")
                else:
                    f.write(f"  Output:\n{stdout}  \n")
            if exit_code != 0:
                f.write(f"  Exit code: {exit_code}  \n")
            if log_time:
                f.write(f"  Runtime: {run_time:.2f} seconds  \n")

    if exit_code > 0:
        log_message('error', stderr)
        sys.exit(stderr)

    return stdout, stderr, exit_code

@log_and_handle_error
def sample_alignment(loci_dir: Path, taxa_list: Path, output_folder: Path, num_aln: int = None, combine_subtree: bool = False, loci_filter: Path = None, nchar_row = None, nchar_col = None) -> None:
    """
    Sample alignments from the given loci directory and subtree directory.

    Args:
        loci_dir (Path): Path to the directory containing loci alignments.
        taxa_list (Path): Path to the directory or file containing taxa for each subtree.
        output_folder (Path): Path to the output folder.
        num_aln (int, optional): Number of alignments to sample. If None, sample all alignments.
        combine_subtree (bool): Whether to combine subtrees into a single file.
        loci_filter (Path, optional): Path to the file containing the list of loci to filter.
    """
    output_folder.mkdir(parents=True, exist_ok=True)  # Create the output folder if it doesn't exist

    def filter_loci_files(loci_dir, loci_filter):
        # Get all loci files in the loci directory
        loci_files = [f for f in loci_dir.glob("*.fa*")]
        if loci_filter and loci_filter.stat().st_size > 0:
            # If a loci filter is provided, read the filtered loci and keep only those in the list
            with open(loci_filter, 'r') as f:
                filtered_loci = f.read().splitlines()
            loci_files = [f for f in loci_files if f.name in filtered_loci]
            log_message('result', f"Discarded {len([f for f in loci_dir.glob('*.fa*') if f.name not in filtered_loci])} loci based on the loci filter.")
        return loci_files

    def run_faSomeRecords(loci_file, taxa_file, output_file, nchar_row = None, nchar_col = None):
        # Run the faSomeRecords command to extract sequences from a loci file based on a taxa file
        cmd = f"faSomeRecords {loci_file} {taxa_file} {output_file}"
        run_command(cmd, f"{output_folder}/log.md", log_any=False)
        # Drop rubbish alignment: remove sequences with less than 5 parsimony informative sites and 3 valid taxa
        # If keep the alignment, delete the row and column with less than nchar_row & nchar_col non-gap characters
        return drop_rubbish_aln(output_file, nchar_row=nchar_row, nchar_col=nchar_col, ntaxa=3, npls_site=5)

    def process_loci_files(loci_files, taxa_list, output_dir, num_aln=None, nchar_row = None, nchar_col = None):
        splited_aln_count, deleted_aln_count = 0, 0
        if taxa_list.is_file():
            # If a single taxa file is provided
            log_message('process', f"Input a single taxa file: {taxa_list}. Sampling sequences for {len(loci_files)} loci.")
            log_message('result', f"Number of input species: {sum(1 for line in open(taxa_list))}")
            for loci_file in loci_files:
                output_file = output_dir / os.path.basename(loci_file)
                if run_faSomeRecords(loci_file, taxa_list, output_file, nchar_row, nchar_col):
                    splited_aln_count += 1
                else:
                    deleted_aln_count += 1
        elif taxa_list.is_dir():
            if combine_subtree:
                # If subtrees need to be combined
                log_message('process', f"Input {len(os.listdir(taxa_list))} subtree files and combine them. Sampling sequences for {len(loci_files)} loci.")
                all_taxa_file = output_dir / "combined_taxa.txt"
                with open(all_taxa_file, 'w') as f:
                    for taxa_file in os.listdir(taxa_list):
                        if taxa_file.endswith(".txt"):
                            with open(taxa_list / taxa_file, 'r') as tf:
                                f.write(tf.read())
                target_aln_count = min(num_aln or len(loci_files), len(loci_files))
                for loci_file in loci_files:
                    output_file = output_dir / os.path.basename(loci_file)
                    if run_faSomeRecords(loci_file, all_taxa_file, output_file, nchar_row, nchar_col):
                        splited_aln_count += 1
                    else:
                        deleted_aln_count += 1
                    if splited_aln_count >= target_aln_count:
                        break
                if num_aln is not None and splited_aln_count < num_aln:
                    log_message('result', f"Could not obtain {num_aln} alignments after combining subtrees. Keeping {splited_aln_count} alignments.")
            else:
                # If subtrees don't need to be combined
                total_aln_count = len(loci_files) * len(os.listdir(taxa_list))
                log_message('process', f"Input {len(os.listdir(taxa_list))} subtree files and {len(loci_files)} loci files. Total number of potential alignments: {total_aln_count}.")
                if num_aln is not None and num_aln < total_aln_count:
                    # If the requested number of alignments is less than the total potential alignments
                    log_message('result', f"Sub-sampling {num_aln} alignments from {total_aln_count} alignments.")
                    subtree_loci_pairs = list(itertools.product(
                        (taxa_list / taxa_file for taxa_file in os.listdir(taxa_list) if taxa_file.endswith(".txt")),
                        loci_files
                    ))
                    print(len(subtree_loci_pairs))
                    random.shuffle(subtree_loci_pairs)  # Shuffle the list to avoid sequential selection
                    target_aln_count = min(num_aln or total_aln_count, total_aln_count)
                    target_aln_count = min(int(target_aln_count * 1.2), total_aln_count)  # 20% spare space, but not exceeding total alignment count
                    for taxa_file, loci_file in subtree_loci_pairs[:target_aln_count]:
                        tree_name = os.path.splitext(os.path.basename(taxa_file))[0]
                        loci_name = os.path.splitext(os.path.basename(loci_file))[0]
                        ext = os.path.splitext(loci_file)[1]
                        output_file = output_dir / f"{tree_name}_{loci_name}{ext}"
                        if run_faSomeRecords(loci_file, taxa_file, output_file, nchar_row, nchar_col):
                            splited_aln_count += 1
                        else:
                            deleted_aln_count += 1
                        if splited_aln_count >= num_aln:
                            break
                    if splited_aln_count < num_aln:
                        log_message('result', f"Could not obtain the requested {num_aln} alignments. Keeping {splited_aln_count} alignments.")
                else:
                    # If all potential alignments need to be processed
                    for taxa_file in os.listdir(taxa_list):
                        if taxa_file.endswith(".txt"):
                            tree_name = os.path.splitext(taxa_file)[0]
                            for loci_file in loci_files:
                                loci_name = os.path.splitext(os.path.basename(loci_file))[0]
                                ext = os.path.splitext(loci_file)[1]
                                output_file = output_dir / f"{tree_name}_{loci_name}{ext}"
                                if run_faSomeRecords(loci_file, taxa_list / taxa_file, output_file, nchar_row, nchar_col):
                                    splited_aln_count += 1
                                else:
                                    deleted_aln_count += 1
                    log_message('result', f"Obtained {splited_aln_count} alignments from all potential alignments.")
        else:
            raise ValueError(f"{taxa_list} is neither a file nor a directory.")

        log_message('process', f"Remaining {splited_aln_count} alignments. Deleted {deleted_aln_count} alignments.")

    loci_files = filter_loci_files(loci_dir, loci_filter)

    if not loci_files:
        raise ValueError("Loci set is empty after filtering. Program will terminate.")
    
    process_loci_files(loci_files, taxa_list, output_folder, num_aln = num_aln, nchar_row = nchar_row, nchar_col = nchar_col)

def get_constraint_tree(loci_dir, subtree_dir, output_tree_path):
    from Bio import Phylo
    from get_subtree import get_subtree_from_fasta
    # Get and arrange aligments by filename
    loci_file_names = os.listdir(loci_dir)
    sorted_loci_file_names = sorted(loci_file_names)

    # Create a dictionary to store the subtree for each file
    tree_dict = {}
    for file in os.listdir(subtree_dir):
        if file.endswith('.tre'):
            with open(os.path.join(subtree_dir, file), 'r') as f:
                tree_name, _ = os.path.splitext(file)
                tree_dict[tree_name] = Phylo.read(f, 'newick')

    # Extract and write trees in the order of sorted_loci_subtree_names
    with open(output_tree_path, 'w') as output_tree:
        for file in sorted_loci_file_names:
                file_path = os.path.join(loci_dir, file)
                subtree_name = re.search('subtree_\d+', file).group()
                get_subtree_from_fasta(tree_dict[subtree_name], file_path, output_tree)

@log_and_handle_error
def initial_data_extraction(args: argparse.Namespace) -> Tuple[Path, Path]:
    """
    Extract training and testing loci for all signed species.
    """
    nchar_keep_col = max(sum(1 for line in open(args.output_dir / "select_id.txt"))//100, 4)
    log_message('process', "Abstract alingment of selected taxa scale in training set:")
    sample_alignment(args.train_loc_path, args.output_dir / "select_id.txt", args.output_dir / "loci" / "training_loci", loci_filter=args.output_dir / "select_loci.txt",num_aln=None, nchar_col=nchar_keep_col)
    log_message('process', "Abstract alingment of selected taxa scale in testing set:")
    sample_alignment(args.test_loc_path, args.output_dir / "select_id.txt", args.output_dir / "loci" / "testing_loci", loci_filter=args.output_dir / "select_loci.txt",num_aln=None, nchar_col=nchar_keep_col)
    
    concat_training_loci = args.output_dir / "loci" / "concat_training_loci.faa"
    log_message('process', "Concatenating training loci...")
    concatenate_seq_dict(str(args.output_dir / "loci" / "training_loci"), str(concat_training_loci))
    concat_testing_loci = args.output_dir / "loci" / "concat_testing_loci.faa"
    log_message('process', "Concatenating testing loci...")
    concatenate_seq_dict(str(args.output_dir / "loci" / "testing_loci"), str(concat_testing_loci))

    return concat_training_loci, concat_testing_loci

def prune_subtrees(args, ref_tree, subtree_dir, num_subtrees, prune_mode):
    """
    Prune subtrees from the filtered all-species tree.

    Args:
        args (argparse.Namespace): Command line arguments.
        prev_tree (Path): Path to the previous iteration's tree.
        iteration_dir (Path): Directory for the current iteration.

    Returns:
        Path: Path to the directory containing pruned subtrees.
    """
    subtree_dir.mkdir(parents=True, exist_ok=True)

    # Run the R script to prune subtrees
    if num_subtrees:
        cmd = f"Rscript prune_subtree.R -t {ref_tree} -l {args.tree_size_lower_lim} -u {args.tree_size_upper_lim} -n {num_subtrees} -o {subtree_dir} -m {prune_mode}"
    else:
         cmd = f"Rscript prune_subtree.R -t {ref_tree} -l {args.tree_size_lower_lim} -u {args.tree_size_upper_lim} -o {subtree_dir} -m {prune_mode}"
    run_command(cmd, f"{args.output_dir}/log.md")

    # Print prune_subtree.R log directly to the log file
    with open(f"{subtree_dir}/summary/prune_log.txt", 'r') as f:
        log_message('result', f.read())
    log_message('result', f"See detailed summary in {subtree_dir / 'summary'}")

    # Remove the mono-furcation nodes in the pruned trees
    for file in subtree_dir.glob("*.tre"):
        try:
            remove_redundant_nodes(file)
        except Exception as e:
            log_message('error', f"Error remove mono-furcation nodes in {file}: {e}")
    return subtree_dir

def test_model(args, output_dir, test_loci_dir, model_name_set, trained_model_nex, mode, loop_id, te=None, initial_tree = None, pre = None):
    """
    Test the model performance on test loci or concatenated alignment.

    Args:
        args (argparse.Namespace): Command line arguments.
        output_dir (Path): Output directory for test results.
        test_loci_dir (Path): Directory containing test loci or a concatenated test set.
        model_name_set (str): Comma-separated list of model names to test.
        trained_model_nex (Path): Path to the trained model nexus file.
        mode (str): Test mode, either "concat" or "partition".
        te (Path, optional): Path to the tree file for the -te option in IQ-TREE.
        initial_tree (Path, optional): Path to the initial tree for the -t option in IQ-TREE to accelerate tree search.
    """
    if te:
        initial_tree = None

    output_dir.mkdir(parents=True, exist_ok=True)
    if mode == "concat":
        if test_loci_dir.is_file():
            concat_test_loci = test_loci_dir
        else:
            # Concatenate test loci into a single alignment
            concat_test_loci = output_dir / "concat_test_loci.faa"
            concatenate_seq_dict(str(test_loci_dir), str(concat_test_loci))
        # Test models on the concatenated alignment
        cmd = f"iqtree -T {args.max_threads} -s {concat_test_loci} -m TESTNEWONLY -mset {model_name_set} -mdef {trained_model_nex}"
    elif mode == "partition":
        # Test models on individual test loci
        cmd = f"iqtree -T {args.max_threads} -p {test_loci_dir} -m TESTNEWONLY -mset {model_name_set} -mdef {trained_model_nex}"
    else:
        log_message('error', "Invalid name of testing method.")
        return
    if te:
        cmd += f" -te {te}"
    if initial_tree:
        cmd += f" -t {initial_tree}"
    test_prefix = f"{output_dir / args.prefix}_test_{mode}"
    step = f"test_{mode}"
    if pre:
        test_prefix = pre
        step = pre
    cmd += f" -pre {test_prefix}"

    run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
    test_iqtree_file = f"{test_prefix}.iqtree"
    log_link('result', f"Detail result of {mode} test", f"{test_prefix}.log")
    write_iqtree_statistic(test_iqtree_file, f"{args.prefix}", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": loop_id, "step": f"{step}"})


    if mode == "concat":
        # Extract model information and print as Markdown table
        with open(test_iqtree_file) as f:
            content = f.read()
        
        model_table_start = content.find("List of models sorted by BIC scores:")
        if model_table_start != -1:
            model_table_end = content.find("AIC, w-AIC", model_table_start) - 1
            model_table = content[model_table_start:model_table_end].strip()

            log_message('result', f"Model testing results ({mode}):")
            log_message('result', "| Model | LogL | BIC |", new_line = True)
            log_message('result', "|-------|------|-----|")

            model_data = []
            for line in model_table.split("\n")[3:]:  # Skip header lines
                if not line.strip():
                    continue
                fields = line.split()
                model, logl, bic = fields[0], fields[1], fields[8]
                model_data.append([model, logl, bic])
                log_message('result', f"| {model} | {logl} | {bic} |")

    if mode == "partition":
        partition_test_nex = f"{test_prefix}.best_scheme.nex"
        best_model_name = run_command(f"./analyze_best_models.sh {partition_test_nex} {output_dir / 'models.txt'}", f"{args.output_dir}/log.md", log_any=False)[0].strip()
        log_message('result', f"Best model for test data:")
        log_message('result', best_model_name)

        # Print best models output as a table
        with open(output_dir / 'models.txt', 'r') as f:
            best_models = [line.strip().split() for line in f]
        
        log_message('result', "| Model | Count |", new_line = True)
        log_message('result', "|-------|-------|")
        
        model_data = []
        for model, count in best_models:
            model_data.append([model, count])
            log_message('result', f"| {model} | {count} |")
        
    return model_data

def compare_trees(args, prev_tree, new_tree, html_output_dir, name):
    cmd_R = f"""
    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '{html_output_dir}', params = list(tree1_path = '{prev_tree}', tree2_path = '{new_tree}', root = FALSE, summary_path = '{args.output_dir}/tree_summary.csv', cophylo_path = '{html_output_dir}/cophylo_plot.pdf', name = '{name}'))"
    """
    run_command(cmd_R, f"{args.output_dir}/log.md")
    log_link('result', "Tree comparison report", str(html_output_dir / "tree_comparison.html"))

    summary_df = pd.read_csv(f"{args.output_dir}/tree_summary.csv")
    current_loop_df = summary_df[summary_df['name'] == name]

    rf_dist = current_loop_df['RF_dist'].values[0]
    nrf_dist = current_loop_df['nRF'].values[0]
    tree1_bl = current_loop_df['Tree1_BL'].values[0]
    tree2_bl = current_loop_df['Tree2_BL'].values[0]

    log_message('result', f"RF distance: {rf_dist}")
    log_message('result', f"Normalized RF distance: {nrf_dist}")
    log_message('result', f"Tree 1 branch length: {tree1_bl}")
    log_message('result', f"Tree 2 branch length: {tree2_bl}")

def logging_cross_test_table(ref_concat_result, final_concat_result):
    """
    Log the cross test results as a 3x3 table.
    """
    def extract_best_bic(model_data):
        """
        Extract the best BIC for inferred and existed models from the model data.
        """
        inferred_bic = float('inf')
        existed_bic = float('inf')
        
        for model, _, bic in model_data:
            bic = float(bic)
            if model.startswith(('d__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__')):
                inferred_bic = min(inferred_bic, bic)
            else:
                existed_bic = min(existed_bic, bic)
        
        return inferred_bic, existed_bic

    # Extract best logL for inferred and existed models
    bic11, bic21 = extract_best_bic(final_concat_result)
    bic12, bic22 = extract_best_bic(ref_concat_result)
    
    # Calculate differences
    tree_diff1 = round(bic11 - bic12, 4)
    tree_diff2 = round(bic21 - bic22, 4)
    model_diff1 = round(bic11 - bic21, 4)
    model_diff2 = round(bic12 - bic22, 4)

    # Determine the signs for tree and model differences
    tree_diff_sign = 'T~'
    if tree_diff1 > 0 and tree_diff2 > 0:
        tree_diff_sign = 'T-'
    elif tree_diff1 < 0 and tree_diff2 < 0:
        tree_diff_sign = 'T+'
    
    model_diff_sign = 'M~'
    if model_diff1 > 0 and model_diff2 > 0:
        model_diff_sign = 'M-'
    elif model_diff1 < 0 and model_diff2 < 0:
        model_diff_sign = 'M+'
    
    # Format the final model_tree_diff
    model_tree_diff = f"{model_diff_sign}/{tree_diff_sign}"
    
    # Print the 2x2 table
    log_message('result', "BIC difference between different models and trees:")
    log_message('result', "| Model | Final best tree | Existing model tree | Tree diff |", new_line = True)
    log_message('result', "|-------|------------|----------------|-----------|")
    log_message('result', f"| Inferred model | {bic11:.4f} | {bic12:.4f} | {tree_diff1:.4f} |")
    log_message('result', f"| Existing model | {bic21:.4f} | {bic22:.4f} | {tree_diff2:.4f} |")
    log_message('result', f"| Model diff | {model_diff1:.4f} | {model_diff2:.4f} | {model_tree_diff} |")
    log_message('result', f"{model_tree_diff} means weather model(M) and tree(T) have same trend in BIC change.(+ final better, - final worse, ~ no trend)")

def create_nexus_partition(input_dir, output_file):
    """
    Creates a NEXUS partition file for IQ-TREE from a directory or list of directories of sequence files.

    Args:
        input_dir (str or list): The directory or list of directories containing sequence files.
        output_file (str): The path to the output NEXUS file.

    Returns:
        None
    """
    # Ensure input_dir is a list
    if isinstance(input_dir, str):
        input_dir = [input_dir]
    
    files = []
    for directory in input_dir:
        files.extend(os.listdir(directory))
    
    with open(output_file, 'w') as f:
        f.write("#nexus\nbegin sets;\n")
        for directory in input_dir:
            for file in os.listdir(directory):
                abs_path = os.path.abspath(os.path.join(directory, file))
                f.write(f"charset {file} = {abs_path}: ;\n")
        f.write("end;\n")


def main(args: argparse.Namespace) -> None:
    """
    Main function to run the model estimation pipeline.

    Args:
        args (argparse.Namespace): Command line arguments.
    """
    PATH_FASTTREEMP = args.FastTreeMP_path
    initial_model_set = args.initial_model_set

    setup_logging(args.output_dir, args.verbose)
    files_to_remove = []

    log_message('process', "## Initialization")
    log_message('result', f"Running model estimation with the following parameters:")
    log_message('result', f"  Maximum iterations: {args.max_iterate}")
    log_message('result', f"  Convergence threshold: {args.converge_thres}")
    log_message('result', f"  File prefix: {args.prefix}")
    log_message('result', f"  Taxa name: {args.taxa_name}")
    log_message('result', f"  Number of training loci: {args.num_aln}")
    log_message('result', f"  Drop species threshold: {args.t_drop_species}")
    log_message('result', f"  Drop locus threshold: {args.t_drop_loc}")
    log_message('result', f"  Initial model set: {initial_model_set}")
    log_message('result', f"  Keep model threshold: {keep_model_thres}")
    log_message('result', f"  Pruning mode: {args.prune_mode}")
    log_message('result', f"  Lower limit for subtree size: {args.tree_size_lower_lim}")
    log_message('result', f"  Upper limit for subtree size: {args.tree_size_upper_lim}")

    log_message('process', "### Quality trimming")
    quality_trimming(args.taxa_file, args.taxa_scale, args.taxa_name, args.output_dir, args.t_drop_loc, args.t_drop_species)

    log_message('process', "### Initial data extraction")
    concat_training_loci, concat_testing_loci = initial_data_extraction(args)
    training_loci_path = args.output_dir / "loci" / "training_loci"
    testing_loci_path = args.output_dir / "loci" / "testing_loci"
    files_to_remove.append(args.output_dir / "loci")
    files_to_remove.append(args.output_dir / "pruned_integrity_table.csv")
    # with open(args.output_dir / "select_id.txt", 'r') as f:
    #     all_species_count = len(f.readlines())

    log_message('process', "### Prune reference tree")
    prune_tree(args.ref_tree, args.output_dir / "select_id.txt", args.output_dir / "ref_tree.tre")
    filtered_allspc_tree = args.output_dir / "ref_tree.tre"

    iteration_id = 1
    prev_model = None
    model_set = initial_model_set
    trained_model_nex = None
    prev_tree = filtered_allspc_tree
    initial_best_model_name = None

    # Create the directory for the output of models
    models_dir = args.output_dir / "inferred_models"
    models_dir.mkdir(exist_ok=True)
    # Create the directory for the output of trees
    trees_dir = args.output_dir / "estimated_tree"
    trees_dir.mkdir(exist_ok=True)
    shutil.copy(filtered_allspc_tree, trees_dir / "pruned_reference_tree.tre")
    
    while True:
        loop_start_time = time.time()
        log_message('process', f"## Iteration {iteration_id}", new_line = True)
        iteration_dir = args.output_dir / f"loop_{iteration_id}"
        iteration_dir.mkdir(parents=True, exist_ok=True)

        # 1. Prune subtrees from the filtered all-species tree
        log_message('process', "### Prune subtrees")
        subtree_dir = iteration_dir / "subtrees"
        # Calculate the number of subtrees to prune
        if args.fix_subtree_num:
            # change 1.0 to keep some spare space
            num_subtrees = math.ceil(args.num_aln * 1.0 / len(list(args.output_dir.glob('loci/training_loci/*.fa*'))))
        else:
            num_subtrees = None
        prune_subtrees(args, prev_tree, subtree_dir, num_subtrees, args.prune_mode)

        # 2. Extract subtree loci from the filtered sequence set using split_loci.sh
        log_message('process', "### Extract subtree loci for trainning")
        sample_alignment(training_loci_path, subtree_dir / "taxa_list", iteration_dir / "training_loci", num_aln=args.num_aln, nchar_row = 3, nchar_col = 1)
        subtree_train_loci_dir = iteration_dir / "training_loci"
        files_to_remove.append(subtree_train_loci_dir)

        # 3. Run ModelFinder to find the best model using the pruned subtrees
        log_message('process', "### Subtree update")
        subtree_update_dir = iteration_dir / "subtree_update"
        subtree_update_dir.mkdir(parents=True, exist_ok=True)
        cmd = f"iqtree -T {args.max_threads} -S {subtree_train_loci_dir} -m MFP -mset {model_set}"
        if trained_model_nex:
            cmd += f" -mdef {trained_model_nex}"
        if args.fix_subtree_topology:
            constraint_tree_path = subtree_update_dir / "constraint_tree.tre"
            get_constraint_tree(subtree_train_loci_dir, subtree_dir, constraint_tree_path)
            # path_to_remove = subtree_update_dir / "constraint_tree2.tre"
            # remove_redundant_nodes(constraint_tree_path, path_to_remove)
            cmd += f" -te {constraint_tree_path}" 
            # cmd += f" -te {path_to_remove}" 

        cmd += f" -pre {subtree_update_dir / args.prefix}"
        run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)

        subtree_update_nex = subtree_update_dir / f"{args.prefix}.best_scheme.nex"
        subtree_iqtree_path = subtree_update_dir / f"{args.prefix}.iqtree"  
        subtree_update_trees = subtree_update_dir / f"{args.prefix}.treefile" 
        write_iqtree_statistic(subtree_iqtree_path, f"{args.prefix}", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": iteration_id, "step": "subtree_update"})
        plot_loci_statistic(subtree_iqtree_path, subtree_update_dir / "loci_statistic.png")
        log_link('result', "Subtree update log", str(subtree_update_dir / f"{args.prefix}.iqtree"))

        # Get the initial best model name
        best_model_name = run_command(f"./analyze_best_models.sh {subtree_update_nex} {subtree_update_dir / 'models.txt'}", f"{args.output_dir}/log.md", log_any=False)[0].strip()
        if iteration_id == 1:
            initial_best_model_name = best_model_name
        log_message('result', f"Best models for iteration {iteration_id}:")
        log_message('result', best_model_name)

        # Print best models output as a table
        with open(subtree_update_dir / 'models.txt', 'r') as f:
            best_models = [line.strip().split() for line in f]
        log_message('result', "| Model | Count |", new_line = True)
        log_message('result', "|-------|-------|")
        for model, count in best_models:
            log_message('result', f"| {model} | {count} |")
        
        # Set prev_model to the best model of past iteration
        if best_model_name in initial_model_set:
            prev_model = extract_spc_Q_from_nex(args.model_dir, best_model_name)
        else:
            prev_model = extract_spc_Q_from_nex(trained_model_nex, best_model_name)

        # Update model_set based on the best models
        best_models_output = subtree_update_dir / 'models.txt'
        with open(best_models_output) as f:
            best_model_counts = {}
            for line in f:
                line = line.strip()
                if line:
                    count, model = line.split()
                    best_model_counts[model] = int(count)

        total_models = sum(best_model_counts.values())
        model_set = ",".join([model for model, count in best_model_counts.items() if count / total_models >= keep_model_thres])

        # 4. Estimate new models using ModelFinder based on the best model for each partition and the pruned subtree
        log_message('process', "### Model update")
        model_update_dir = iteration_dir / "model_update"
        model_update_dir.mkdir(parents=True, exist_ok=True)
        if not trained_model_nex:
            cmd = f"iqtree -T {args.max_threads} -S {subtree_update_nex} -te {subtree_update_trees} --model-joint GTR20+FO --init-model {best_model_name} -pre {model_update_dir / args.prefix}"  
        else:
            cmd = f"iqtree -T {args.max_threads} -S {subtree_update_nex} -te {subtree_update_trees} --model-joint GTR20+FO --init-model {best_model_name} -mdef {trained_model_nex} -pre {model_update_dir / args.prefix}"
        run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)

        model_iqtree_file = model_update_dir / f"{args.prefix}.iqtree"
        log_link('result', "Model update log", str(model_update_dir / f"{args.prefix}.iqtree"))
        model_stats = write_iqtree_statistic(model_iqtree_file, f"{args.prefix}", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": iteration_id, "step": "model_update"})
        log_message('result', f"BIC of the new model: {model_stats['BIC']}")  
        log_message('result', f"Likelihood of the new model: {model_stats['log_likelihood']}")

        trained_model_nex = models_dir / "trained_model.nex"

        # Extract the Q matrix from the IQ-TREE output file
        new_model = extract_Q_from_iqtree(f"{args.prefix}_{iteration_id}", model_iqtree_file)
        # Convert the Q matrix to the format required by FastTree
        new_model.convert_to_fasttree(model_update_dir)  
        # Check if the new model match the signle-precision requirement
        if not new_model.check_precision(threshold=1e-8):
            log_message('error', "Model does not meet precision requirement.")
        # Add the Q matrix to the nexus file containing trained models
        new_model.add_Q_to_nex(trained_model_nex)

        # Update model_set for next iteration
        if iteration_id > 1:
            model_set = f"{initial_model_set},{new_model.model_name}"  
        else:
            model_set += f",{new_model.model_name}"

        log_link('result', "New model", str(models_dir / f"{new_model.model_name}"))
        log_message('result', f"Model set for next iteration: {model_set}")

        # Save the model parameters to a file in the output directory
        with open(models_dir / f"{new_model.model_name}", 'w') as f:
            f.write(new_model.print_parameter())

        # Compare the current model with the previous model using bubble plot
        bubble_plot(new_model, iteration_dir / f"{args.prefix}_model_{iteration_id}.png")
        log_link('result', "Model bubble plot", str(iteration_dir / f"{args.prefix}_model_{iteration_id}.png"))
        if prev_model:
            bubble_difference_plot(prev_model, new_model, iteration_dir / f"model_diff_{iteration_id}.png")
            log_link('result', "Model difference plot", str(iteration_dir / f"model_diff_{iteration_id}.png"))
        
        # Generate summary for model update
        if args.model_update_summary:
            summary_dir = model_update_dir / "summary"
            summary_dir.mkdir(exist_ok=True)
            subtree_log_path = subtree_update_dir / f"{args.prefix}.log"
            model_log_path = model_update_dir / f"{args.prefix}.log"
            cmd = f"Rscript model_update_summary.R {subtree_iqtree_path} {subtree_log_path} {model_log_path} {summary_dir}"
            log_message('process', "Generated summary for model update, see" + str(summary_dir))
            run_command(cmd, f"{args.output_dir}/log.md")

        # 5. Check for model convergence
        log_message('process', "### Check model convergence")
        log_message('process', f"Iteration {iteration_id}: Checking convergence")
        ifconverge, corr, dist = prev_model.check_convergence(new_model, threshold=args.converge_thres)
        log_message('result', f"Pearson's correlation: {corr}")  
        log_message('result', f"Euclidean distance: {dist}")

        if ifconverge:
            # If convergence is reached, stop the iteration
            log_message('result', f"Convergence of model reached at iteration {iteration_id}")
            break
        
        # 6. Re-estimate the tree using FastTree on the concatenated loci
        log_message('process', "### Tree update")
        tree_update_dir = iteration_dir / "tree_update"
        tree_update_dir.mkdir(parents=True, exist_ok=True)

        # Set the number of threads for fasttree to 3
        os.environ['OMP_NUM_THREADS'] = '3'
        cmd_FT = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {tree_update_dir}/fasttree.log -intree {filtered_allspc_tree} {concat_training_loci} > {tree_update_dir / args.prefix}_{iteration_id}.treefile"
        run_command(cmd_FT, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)

        log_link('result', "FastTree log", str(tree_update_dir / "fasttree.log"))

        new_tree = tree_update_dir / f"{args.prefix}_{iteration_id}.treefile"
        shutil.copy(new_tree, trees_dir / f"Loop_{iteration_id}_FT_Train_G20.treefile")
        compare_trees(args, prev_tree, new_tree, iteration_dir, f"loop_{iteration_id}")

        # 7. Verify the performance of new and old models using ModelFinder
        if args.test_in_loop:
            inloop_test_dir = iteration_dir / "test_model"
            inloop_test_dir.mkdir(parents=True, exist_ok=True)
            log_message('process', "### Test model performance")
            test_model(args, inloop_test_dir, concat_testing_loci, model_set, trained_model_nex, "concat", loop_id = iteration_id, te=new_tree)

        iteration_id += 1
        prev_model = new_model
        prev_tree = new_tree

        loop_end_time = time.time()
        loop_time = loop_end_time - loop_start_time
        log_message('process', f"Time usage for Loop_{iteration_id}: {loop_time:.2f} seconds ({loop_time/3600:.2f} h)")

        if iteration_id > args.max_iterate:
            # If the maximum number of iterations is reached, stop the iteration
            log_message('result', f"Stop loop after {args.max_iterate} times of iteration")
            break
    
    # Final model testing
    log_message('process', "## Final test", new_line = True)
    final_test_dir = args.output_dir / "final_test"
    final_test_dir.mkdir(parents=True, exist_ok=True)
    final_test_logdir = final_test_dir / "logfiles"
    final_test_logdir.mkdir(exist_ok=True)

    # 1. Estimate the best final tree on the concatenated loci
    if args.estimate_best_final_tree or args.test_final_tree or args.cross_validation:
        log_message('process', "### Final tree estimation on all loci")
        if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
            all_loci_partition_nex = final_test_logdir / "all_loci_partition.nex"
            create_nexus_partition([training_loci_path, testing_loci_path], all_loci_partition_nex)
            cmd = f"iqtree -T {args.max_threads} -p {all_loci_partition_nex} -t {new_tree} -m MFP -mset {model_set} -mdef {trained_model_nex} -pre {final_test_logdir}/best_final_tree"
            if args.final_tree_tool == "IQFAST":
                cmd += " -fast" 
        else:
            concat_all_loci = final_test_dir / "all_loci.faa"
            concatenate_seq_list([concat_training_loci, concat_testing_loci], concat_all_loci)
            files_to_remove.append(concat_all_loci)
            cmd = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/best_final_tree.log -intree {new_tree} {concat_training_loci} > {final_test_logdir}/best_final_tree.treefile"
        run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
        new_tree = final_test_logdir / "best_final_tree.treefile"
        if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
            final_tree_info = write_iqtree_statistic(f"{final_test_logdir}/best_final_tree.iqtree" ,args.prefix , f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": "Final test", "step": "Final best tree"})
            final_tree_ll = final_tree_info['log_likelihood']
            shutil.copy(new_tree, trees_dir / f"FinalModel_IQ_All_partition.treefile")
        else:
            shutil.copy(new_tree, trees_dir / f"FinalModel_FT_All_G20.treefile")
        
    # 2. Compare the reference tree and the final tree
    log_message('process', "### Tree comparison")
    log_message('result', "Compare the final tree with reference tree:")
    compare_trees(args, filtered_allspc_tree, new_tree, args.output_dir, "final_tree_compare")

    # 3. Compare the initial best model and the final model
    if initial_best_model_name:
        log_message('process', "### Model comparison")
        initial_best_model = extract_spc_Q_from_nex(args.model_dir, initial_best_model_name)
        ifconverge, corr, dist = initial_best_model.check_convergence(new_model, threshold=args.converge_thres)
        log_message('result', f"Comparison between initial best model ({initial_best_model_name}) and final model ({new_model.model_name}):")
        log_message('result', f"Pearson's correlation: {corr}")  
        log_message('result', f"Euclidean distance: {dist}")  
        bubble_plot(initial_best_model, final_test_dir / "initial_best_model.png")
        log_link('result', "Initial best model bubble plot", str(final_test_dir / "initial_best_model.png"))
        bubble_plot(new_model, final_test_dir / "final_model.png")
        log_link('result', "Final model bubble plot", str(final_test_dir / "final_model.png"))
        bubble_difference_plot(initial_best_model, new_model, final_test_dir / "model_comparison.png")
        log_link('result', "Model comparison plot", str(final_test_dir / "model_comparison.png"))

    # 4. Plot PCA of Q matrices and state frequencies among initial and trained models
    log_message('process', "### PCA Plot for all models")
    cmd = f"Rscript PCA_Q.R {args.model_dir} {models_dir}/trained_model.nex {models_dir}"
    run_command(cmd, f"{args.output_dir}/log.md")
    log_link('result', "PCA plot of Q matrices", str(models_dir / "PCA_Q.png"))
    log_link('result', "PCA plot of state frequencies", str(models_dir / "PCA_F.png"))

    # 5. Test the final model on partitioned test loci without providing the constraint tree
    if args.test_partition_test_loci:
        log_message('process', "### Final model testing on partitioned test loci without constraint tree")
        partition_test_result = test_model(args, final_test_logdir, testing_loci_path, model_set, trained_model_nex, "partition", loop_id="final_test_partition", initial_tree=new_tree)

    # 6. Validate the final model in subtrees on testing loci
    if args.test_subtrees:
        log_message('process', "### Final model testing of test loci in subtrees")
        log_message('process', "#### Extract subtree loci for testing")
        subtree_test_loci_dir = final_test_logdir / "testing_alignment"
        files_to_remove.append(subtree_test_loci_dir)
        prune_subtrees(args, new_tree, final_test_logdir / "subtrees", num_subtrees=None, prune_mode="random")
        sample_alignment(testing_loci_path, final_test_logdir / "subtrees" / "taxa_list", subtree_test_loci_dir, nchar_row=3, nchar_col=1)
        log_message('process', "#### Test model performance")
        test_model(args, final_test_logdir, subtree_test_loci_dir, model_set, trained_model_nex, "partition", loop_id="final_test_subtrees", te=None)

    # 7. Validate the final model in concatenated testing loci
    log_message('process', "### Final model testing of concatenated test loci on final tree")
    final_concat_result = test_model(args, final_test_logdir, concat_testing_loci, model_set, trained_model_nex, "concat", loop_id="final_test_concat", te=new_tree)
    # If the final model has better BIC than the existing models, continue to estimate the final tree on all loci
    if final_concat_result:
        best_concat_test_model = min(final_concat_result, key=lambda x: float(x[2]))  # Find the model with the lowest BIC value
        if not best_concat_test_model[0].startswith(('d__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__')):
            log_message('error', f"Warning: The inferred model is not better based on BIC value than the existing models.")
        else:
            log_message('process', f"The inferred model is better based on BIC value than the existing models.")

            # 7. If the final model is better than the existing models in the concatenated test loci, perform cross-validation
            if args.test_final_tree or args.cross_validation:
                log_message('process', "### Test final tree")
                log_message('process', "#### Final tree estimation on all loci without inferred model")
                if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
                    existing_model_tree = final_test_logdir / "existing_model_tree.treefile"
                    cmd = f"iqtree -T {args.max_threads} -p {all_loci_partition_nex} -t {new_tree} -m MFP -mset {initial_model_set} -pre {final_test_logdir}/existing_model_tree"
                    if args.final_tree_tool == "IQFAST":
                        cmd += " -fast"
                    run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                    shutil.copy(existing_model_tree, trees_dir / f"ExistModel_IQ_All_partition.treefile")
                else:
                    cmd = f"{PATH_FASTTREEMP} -wag -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/allloci_wag_tree.log -intree {new_tree} {concat_training_loci} > {final_test_logdir}/allloci_wag_tree.treefile"
                    run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                    shutil.copy(f"{final_test_logdir}/allloci_wag_tree.treefile", trees_dir / f"FT_All_WAG_G20.treefile")
                    cmd = f"{PATH_FASTTREEMP} -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/allloci_lg_tree.log -intree {new_tree} {concat_training_loci} > {final_test_logdir}/allloci_lg_tree.treefile"
                    run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                    shutil.copy(f"{final_test_logdir}/allloci_lg_tree.treefile", trees_dir / f"FT_All_LG_G20.treefile")
                    wag_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_wag_tree.log")
                    lg_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_lg_tree.log")
                    existing_tree_ll = max(wag_tree_ll, lg_tree_ll)
                    if wag_tree_ll >= lg_tree_ll:
                        existing_model_tree = final_test_logdir / "allloci_wag_tree.treefile"
                        log_message('result', f"WAG model has higher likelihood than LG model, use WAG model for final tree.")
                    else:
                        existing_model_tree = final_test_logdir / "allloci_lg_tree.treefile"
                        log_message('result', f"LG model has higher likelihood than WAG model, use LG model for final tree.")

                log_message('process', "#### Compare final tree with existing model tree")
                compare_trees(args, existing_model_tree, new_tree, final_test_dir, "compare_existing_model_tree")
                # Compare LogL for the final model tree and the existing model tree
                if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
                    existing_tree_info = write_iqtree_statistic(f"{final_test_logdir}/existing_model_tree.iqtree", args.prefix, f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": "Final test", "step": "Existing model tree"})
                    existing_tree_ll = existing_tree_info['log_likelihood']
                else:
                    final_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/best_final_tree.log")
                log_message('result', f"Log-Likelihood of final best tree and the tree estimated without inferred model:")

                # log Log-likelihood for final tree and existing tree
                log_message('result', "| Tree | Best final tree | Existing model tree |", new_line=True)
                log_message('result', "|------|-----------------|---------------------|")
                log_message('result', f"| LogL | {final_tree_ll} | {existing_tree_ll} |")
                if final_tree_ll <= existing_tree_ll:
                    log_message('error', "The final model tree does not have better likelihood than the existing model tree.")
                else:
                    log_message('process', "The final model tree has better likelihood than the existing model tree.")
                    # If the final model has better LogL, carry out cross-validation
                    if args.cross_validation:
                        cross_validation_dir = final_test_dir / "cross_validation"
                        cross_validation_dir.mkdir(parents=True, exist_ok=True)
                        log_message('process', "### Cross validation")
                        # Use a temporary directory to store the results of the reference tree test
                        log_message('process', "#### All models testing on existing model tree and all loci")
                        if not args.final_tree_tool == "FT":
                            concat_all_loci = final_test_dir / "all_loci.faa"
                            concatenate_seq_list([concat_training_loci, concat_testing_loci], concat_all_loci)
                        existing_concat_result = test_model(args, cross_validation_dir, concat_all_loci, model_set, trained_model_nex, "concat", loop_id="cross_existing_model_tree", te=existing_model_tree, pre=f"{cross_validation_dir}/cross_existing_model_tree")
                        # Compare the results of the two tests
                        log_message('process', "#### All models testing on final best tree and all loci")
                        final_concat_result = test_model(args, cross_validation_dir, concat_all_loci, model_set, trained_model_nex, "concat", loop_id="cross_final_tree", te=new_tree, pre=f"{cross_validation_dir}/cross_final_tree")
                        logging_cross_test_table(existing_concat_result, final_concat_result)

    # 8. Plot RF and nRF distance among estimated trees and reference tree
    cmd = f"Rscript ./analysis/write_pairwise_tree_dist.R {trees_dir}"
    run_command(cmd, f"{args.output_dir}/log.md", log_any=False)
    log_link('result', "Heatmap of RF distance of trees:", str(trees_dir / "RF_dist.png"))
    log_link('result', "Heatmap of nRF distance of trees:", str(trees_dir / "nRF_dist.png"))
    log_link('result', "Pairwise tree distance metrics: ", str(trees_dir / "tree_pairwise_compare.csv"))

    # 9. Generate summary for final test
    log_message('process', "### Record files")
    log_link('result', "Summary of IQ-TREE result", str(args.output_dir / "iqtree_results.csv"))
    log_link('result', "Summary of tree comparison", str(args.output_dir / "tree_summary.csv"))

    if not args.keep_tmp:
        for file_path in files_to_remove:
            if file_path.is_file():
                os.remove(file_path)
            elif file_path.is_dir():
                shutil.rmtree(file_path, ignore_errors=True)


def cli() -> argparse.Namespace:
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--taxa_name', type=str, required=True, help='Taxonomic name for analysis')
    parser.add_argument('-s', '--taxa_scale', type=str, required=True, help='Taxonomic scale for analysis')
    parser.add_argument('-N', '--num_aln', type=int, required=True, help='Number of training loci')
    parser.add_argument('-a', '--train_loc_path', type=Path, required=True, help='Path to the training loci directory')
    parser.add_argument('-e', '--test_loc_path', type=Path, required=True, help='Path to the testing loci directory')
    parser.add_argument('-f', '--taxa_file', type=Path, required=True, help='Path to the reference taxa information file')
    parser.add_argument('-r', '--ref_tree', type=Path, required=True, help='Path to the reference tree file')
    parser.add_argument('-m', '--model_dir', type=Path, required=True, help='Directory containing initial model files')
    parser.add_argument('-M', '--initial_model_set', type=str, default="LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART", help='Initial model set for ModelFinder (default: LG,Q.PFAM,Q.INSECT,Q.PLANT,Q.YEAST,MTMET,MTART)')
    parser.add_argument('--t_drop_species', type=float, default=0.5, help='Threshold of sequence integrity for dropping species (default: 0.5)')
    parser.add_argument('--t_drop_loc', type=float, default=0.2, help='Threshold of sequence integrity for dropping loci (default: 0.5)')

    parser.add_argument('-T', '--max_threads', type=str, default="100", help='Maximum number of threads (default: 100)')
    parser.add_argument('-l', '--max_iterate', type=int, default=5, help='Maximum number of iterations (default: 5)')
    parser.add_argument('-V', '--converge_thres', type=float, default=0.999, help='Convergence threshold of Q matrix (default: 0.999)')
    parser.add_argument('-p', '--prefix', type=str, default='Q', help='Prefix for output files (default: Q)')

    parser.add_argument('--test_in_loop', action='store_true', help='Test new estimated model with test data in each loop')
    parser.add_argument('--test_subtrees', action='store_true', help='Test the final model on test loci in subtrees')
    parser.add_argument('--test_partition_test_loci', action='store_true', help='Test the final model on partitioned test loci without providing the constraint tree')
    parser.add_argument('--estimate_best_final_tree', action='store_true', help='Estimate the best final tree based on both training and testing loci in partition model')
    parser.add_argument('--test_final_tree', action='store_true', help='Test the final best tree, compare with the tree inferred without the inferred model')
    parser.add_argument('--cross_validation', action='store_true', help='Test the performance of final model and tree on all loci with comparison with initial model and tree estimated without inferred model.')
    parser.add_argument('--final_tree_tool', type=str, default='IQFAST', choices=['IQ',"IQFAST",'FT'], help='Method to estimate the final tree (IQ-TREE[IQ] / IQ-TREE in -fast option [IQFAST] / FastTree[FT]) (default: IQ)')
    parser.add_argument('--fix_subtree_num', action='store_true', help='Fix the number of subtrees during model estimation')
    parser.add_argument('--fix_subtree_topology', action='store_true', help='Fix the topology of subtrees during model estimation')

    parser.add_argument('--tree_size_lower_lim', type=int, default=20, help='Lower limit for the size of subtrees (default: 20)')
    parser.add_argument('--tree_size_upper_lim', type=int, default=100, help='Upper limit for the size of subtrees (default: 100)')  
    parser.add_argument('--prune_mode', type=str, default='random', choices=['random', 'lower', 'upper', 'shallow'], help="Pruning mode (random/lower/upper/shallow) (default: random)")

    parser.add_argument('-S', '--model_update_summary', action='store_true', help='Enable model update summary inner each iteration')
    parser.add_argument('-R', '--tree_comparison_report', action='store_true', help='Enable tree comparison report when comparing pair of trees')
    parser.add_argument('-c', '--keep_cmd_output', action='store_true', help='Keep detailed command output in the log file')
    parser.add_argument('-t', '--keep_tmp', action='store_true', help='Keep temporary files')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print commands')

    parser.add_argument('--output_dir', type=Path, required=True, help='Output directory')
    parser.add_argument('--FastTreeMP_path', type=Path, required=True, help='Path to the FastTreeMP executable')
    return parser.parse_args() 

if __name__ == "__main__":
    args = cli()
    # args.prefix = f"{args.taxa_name}_{args.num_aln}"
    args.prefix = f"{args.taxa_name}_{args.tree_size_upper_lim}"
    args.output_dir = args.output_dir / f"{args.prefix}"  
    args.output_dir.mkdir(parents=True, exist_ok=True)
    start_time = time.time()
    main(args)
    end_time = time.time()
    total_time = end_time - start_time
    log_message('result', f"Total time usage: {total_time:.2f} seconds ({total_time/3600:.2f} h)")