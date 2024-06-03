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
from concat_seq import concatenate_sequences
from get_subtree import prune_tree
from mdlogger import *
from fasta_filter import drop_rubbish_aln

# Define constants
t_drop_species = 0.5
t_drop_loc = 0.1
initial_model_set = "LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART"
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
                f.write(f"  Error:\n{stderr}")
            if log_output and stdout:
                # Sometimes it's annoying some output was interpreted as error(e.g. Rscript)
                if stderr and exit_code == 0:
                    f.write(f"  Output:\n{stderr}\n{stdout}")
                else:
                    f.write(f"  Output:\n{stdout}")
            if exit_code != 0:
                f.write(f"  Exit code: {exit_code}\n")
            if log_time:
                f.write(f"  Runtime: {run_time:.2f} seconds\n")

    if exit_code > 0:
        log_message('error', stderr)
        sys.exit(stderr)

    return stdout, stderr, exit_code

@log_and_handle_error
def sample_alignment(loci_dir: Path, taxa_list: Path, output_folder: Path, num_aln: int = None, combine_subtree: bool = False, loci_filter: Path = None) -> None:
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

    def run_faSomeRecords(loci_file, taxa_file, output_file):
        # Run the faSomeRecords command to extract sequences from a loci file based on a taxa file
        cmd = f"faSomeRecords {loci_file} {taxa_file} {output_file}"
        run_command(cmd, f"{output_folder}/log.md", log_any=False)
        # Drop rubbish alignment: remove sequences with less than 5 parsimony informative sites and 3 valid taxa
        # If keep the alignment, delete the row and column with less than nchar_row & nchar_col non-gap characters
        return drop_rubbish_aln(output_file, nchar_row=4, nchar_col=1, ntaxa=3, npls_site=5)

    def process_loci_files(loci_files, taxa_list, output_dir, num_aln=None):
        splited_aln_count, deleted_aln_count = 0, 0
        if taxa_list.is_file():
            # If a single taxa file is provided
            log_message('process', f"Input a single taxa file: {taxa_list}. Sampling sequences for {len(loci_files)} loci.")
            log_message('result', f"Number of input species: {sum(1 for line in open(taxa_list))}")
            for loci_file in loci_files:
                output_file = output_dir / os.path.basename(loci_file)
                if run_faSomeRecords(loci_file, taxa_list, output_file):
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
                    if run_faSomeRecords(loci_file, all_taxa_file, output_file):
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
                        if run_faSomeRecords(loci_file, taxa_file, output_file):
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
                                if run_faSomeRecords(loci_file, taxa_list / taxa_file, output_file):
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
    
    process_loci_files(loci_files, taxa_list, output_folder, num_aln=num_aln)

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
    log_message('process', "Abstract alingment of selected taxa scale in training set:")
    sample_alignment(args.train_loc_path, args.output_dir / "select_id.txt", args.output_dir / "loci" / "training_loci", loci_filter=args.output_dir / "select_loci.txt", combine_subtree=True)  # Replacing split_loci
    log_message('process', "Abstract alingment of selected taxa scale in testing set:")
    sample_alignment(args.test_loc_path, args.output_dir / "select_id.txt", args.output_dir / "loci" / "testing_loci", loci_filter=args.output_dir / "select_loci.txt", num_aln=None, combine_subtree=True)  # Replacing split_loci
    
    concat_training_loci = args.output_dir / "loci" / "concat_training_loci.faa"
    log_message('process', "Concatenating training loci...")
    concatenate_sequences(str(args.output_dir / "loci" / "training_loci"), str(concat_training_loci))
    concat_testing_loci = args.output_dir / "loci" / "concat_testing_loci.faa"
    log_message('process', "Concatenating testing loci...")
    concatenate_sequences(str(args.output_dir / "loci" / "testing_loci"), str(concat_testing_loci))

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
        cmd = f"Rscript prune_subtree_2.R -t {ref_tree} -l {args.tree_size_lower_lim} -u {args.tree_size_upper_lim} -n {num_subtrees} -o {subtree_dir} -m {prune_mode}"
    else:
         cmd = f"Rscript prune_subtree_2.R -t {ref_tree} -l {args.tree_size_lower_lim} -u {args.tree_size_upper_lim} -o {subtree_dir} -m {prune_mode}"
    run_command(cmd, f"{args.output_dir}/log.md")

    # Print prune_subtree.R log directly to the log file
    with open(f"{subtree_dir}/summary/prune_log.txt", 'r') as f:
        log_message('result', f.read())
    log_message('result', f"See detailed summary in {subtree_dir / 'summary'}")

    return subtree_dir

def test_model(args, output_dir, test_loci_dir, model_name_set, trained_model_nex, mode, loop_id, te=None):
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
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    if mode == "concat":
        if test_loci_dir.is_file():
            concat_test_loci = test_loci_dir
        else:
            # Concatenate test loci into a single alignment
            concat_test_loci = output_dir / "concat_test_loci.faa"
            concatenate_sequences(str(test_loci_dir), str(concat_test_loci))
        # Test models on the concatenated alignment
        cmd = f"iqtree -T {args.max_threads} -s {concat_test_loci} -m TESTONLY -mset {model_name_set} -mdef {trained_model_nex}"
    elif mode == "partition":
        # Test models on individual test loci
        cmd = f"iqtree -T {args.max_threads} -S {test_loci_dir} -m TESTONLY -mset {model_name_set} -mdef {trained_model_nex}"
    else:
        log_message('error', "Invalid name of testing method.")
        return
    if te:
        cmd += f" -te {te}"
    test_prefix = f"{output_dir / args.prefix}_test_{mode}"
    cmd += " -pre " + test_prefix

    run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
    test_iqtree_file = f"{test_prefix}.iqtree"
    write_iqtree_statistic(test_iqtree_file, f"{args.prefix}", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": loop_id, "step": f"test_{mode}"})


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

            for line in model_table.split("\n")[3:]:  # Skip header lines
                if not line.strip():
                    continue
                fields = line.split()
                model, logl, bic = fields[0], fields[1], fields[8]
                log_message('result', f"| {model} | {logl} | {bic} |")

    if mode == "partition":
        partition_test_nex = f"{test_prefix}.best_scheme.nex"
        best_model_name = run_command(f"./analyze_best_models.sh {partition_test_nex} {output_dir / 'models.txt'}", f"{args.output_dir}/log.md", log_any=False)[0].strip()
        log_message('result', f"Best models for test data:")
        log_message('result', best_model_name)

        # Print best models output as a table
        with open(output_dir / 'models.txt', 'r') as f:
            best_models = [line.strip().split() for line in f]
        log_message('result', "| Model | Count |", new_line = True)
        log_message('result', "|-------|-------|")
        for model, count in best_models:
            log_message('result', f"| {model} | {count} |")

def compare_trees(args, prev_tree, new_tree, iteration_dir, name):
    cmd_R = f"""
    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '{iteration_dir}', params = list(tree1_path = '{prev_tree}', tree2_path = '{new_tree}', root = FALSE, summary_path = '{args.output_dir}/tree_summary.csv', name = '{name}'))"
    """
    run_command(cmd_R, f"{args.output_dir}/log.md")
    log_link('result', "Tree comparison report", str(iteration_dir / "tree_comparison.html"))

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

def main(args: argparse.Namespace) -> None:
    """
    Main function to run the model estimation pipeline.

    Args:
        args (argparse.Namespace): Command line arguments.
    """
    PATH_FASTTREEMP = args.FastTreeMP_path

    setup_logging(args.output_dir, args.verbose)
    files_to_remove = []

    log_message('process', "## Initialization")
    log_message('result', f"Running model estimation with the following parameters:")
    log_message('result', f"  Maximum iterations: {args.max_iterate}")
    log_message('result', f"  Convergence threshold: {args.converge_thres}")
    log_message('result', f"  File prefix: {args.prefix}")
    log_message('result', f"  Taxa name: {args.taxa_name}")
    log_message('result', f"  Number of training loci: {args.num_aln}")
    log_message('result', f"  Drop species threshold: {t_drop_species}")
    log_message('result', f"  Drop locus threshold: {t_drop_loc}")
    log_message('result', f"  Initial model set: {initial_model_set}")
    log_message('result', f"  Keep model threshold: {keep_model_thres}")
    log_message('result', f"  Pruning mode: {args.prune_mode}")
    log_message('result', f"  Lower limit for subtree size: {args.tree_size_lower_lim}")
    log_message('result', f"  Upper limit for subtree size: {args.tree_size_upper_lim}")

    log_message('process', "### Quality trimming")
    quality_trimming(args.taxa_file, args.taxa_scale, args.taxa_name, args.output_dir, t_drop_loc, t_drop_species)

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

    (args.output_dir / "trained_models").mkdir(exist_ok=True)
    
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
        sample_alignment(training_loci_path, subtree_dir / "taxa_list", iteration_dir / "training_loci", loci_filter=args.output_dir / "select_loci.txt", num_aln=args.num_aln)
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
            get_constraint_tree(subtree_train_loci_dir, subtree_dir, subtree_update_dir / "constraint_tree.tre")
            cmd += f" -te {subtree_update_dir / 'constraint_tree.tre'}"
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

        trained_model_nex = args.output_dir / "trained_models" / "trained_model.nex"

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

        log_link('result', "New model", str(args.output_dir / "trained_models" / f"{new_model.model_name}"))
        log_message('result', f"Model set for next iteration: {model_set}")

        # Save the model parameters to a file in the output directory
        with open(args.output_dir / "trained_models" / f"{new_model.model_name}", 'w') as f:
            f.write(new_model.print_parameter())

        # Compare the current model with the previous model using bubble plot
        bubble_plot(new_model, iteration_dir / f"{args.prefix}_model_{iteration_id}.png")
        log_link('result', "Model bubble plot", str(iteration_dir / f"{args.prefix}_model_{iteration_id}.png"))
        if prev_model:
            bubble_difference_plot(prev_model, new_model, iteration_dir / f"model_diff_{iteration_id}.png")
            log_link('result', "Model difference plot", str(iteration_dir / f"model_diff_{iteration_id}.png"))

        # 5. Re-estimate the tree using FastTree on the concatenated loci
        log_message('process', "### Tree update")
        tree_update_dir = iteration_dir / "tree_update"
        tree_update_dir.mkdir(parents=True, exist_ok=True)

        # Set the number of threads for fasttree to 3
        os.environ['OMP_NUM_THREADS'] = '3'
        cmd_FT = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {tree_update_dir}/fasttree.log -intree {filtered_allspc_tree} {concat_training_loci} > {tree_update_dir / args.prefix}_{iteration_id}.treefile"
        run_command(cmd_FT, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)

        log_link('result', "FastTree log", str(tree_update_dir / "fasttree.log"))

        new_tree = tree_update_dir / f"{args.prefix}_{iteration_id}.treefile"
        compare_trees(args, prev_tree, new_tree, iteration_dir, f"loop_{iteration_id}")

        # 7. Check for model convergence
        log_message('process', "### Check convergence")
        log_message('process', f"Iteration {iteration_id}: Checking convergence")
        ifconverge, corr, dist = prev_model.check_convergence(new_model, threshold=args.converge_thres)
        log_message('result', f"Pearson's correlation: {corr}")  
        log_message('result', f"Euclidean distance: {dist}")

        loop_end_time = time.time()
        loop_time = loop_end_time - loop_start_time
        log_message('process', f"Time usage for Loop_{iteration_id}: {loop_time:.2f} seconds ({loop_time/3600:.2f} h)")

        if ifconverge:
            # If convergence is reached, stop the iteration
            log_message('result', f"Convergence reached at iteration {iteration_id}")
            break

        # 6. Verify the performance of new and old models using ModelFinder
        if args.test_in_loop:
            inloop_test_dir = iteration_dir / "test_model"
            inloop_test_dir.mkdir(parents=True, exist_ok=True)
            log_message('process', "### Test model performance")
            test_model(args, inloop_test_dir, concat_testing_loci, model_set, trained_model_nex, "concat", loop_id = iteration_id, te=new_tree)

        iteration_id += 1
        prev_model = new_model
        prev_tree = new_tree

        if iteration_id > args.max_iterate:
            # If the maximum number of iterations is reached, stop the iteration
            log_message('result', f"Stop loop after {args.max_iterate} times of iteration")
            break

    # Final model testing
    log_message('process', "## Final test", new_line = True)
    final_test_dir = args.output_dir / "final_test"
    final_test_dir.mkdir(parents=True, exist_ok=True)

    # 1. Compare the reference tree and the final tree
    log_message('process', "### Tree comparison")
    compare_trees(args, filtered_allspc_tree, new_tree, final_test_dir, "final_test")

    # 2. Compare the initial best model and the final model
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

    # 2. Extract subtrees for testing loci and test
    if args.test_partition:
        log_message('process', "### Final model testing of test loci in subtrees")
        log_message('process', "#### Extract subtree loci for testing")
        subtree_test_loci_dir = final_test_dir / "testing_alignment"
        files_to_remove.append(subtree_test_loci_dir)
        prune_subtrees(args, new_tree, final_test_dir / "subtrees", num_subtrees = None, prune_mode = "random")
        sample_alignment(testing_loci_path, final_test_dir / "subtrees" / "taxa_list", subtree_test_loci_dir, loci_filter=args.output_dir / "select_loci.txt")
        log_message('process', "#### Test model performance")
        test_model(args, final_test_dir, subtree_test_loci_dir, model_set, trained_model_nex, "partition", loop_id = "final_test_partition", te=None)
    log_message('process', "### Final model testing of concatenated test loci")
    test_model(args, final_test_dir, concat_testing_loci, model_set, trained_model_nex, "concat", loop_id = "final_test_concat", te=new_tree)

    log_message('process', "### PCA Plot for all models")
    # 3. Plot PCA of Q matrices and state frequencies among initial and trained models
    cmd = f"Rscript PCA_Q.R {args.model_dir} {args.output_dir}/trained_models/trained_model.nex {args.output_dir}/trained_models"
    run_command(cmd, f"{args.output_dir}/log.md")
    log_link('result', "PCA plot of Q matrices", str(args.output_dir / "trained_models" / "PCA_Q.png"))
    log_link('result', "PCA plot of state frequencies", str(args.output_dir / "trained_models" / "PCA_F.png"))
    log_message('process', "### Record files")
    log_link('result', "Summary of IQtree result", str(args.output_dir / "iqtree_results.csv"))
    log_link('result', "Summary of tree comparison", str(args.output_dir / "tree_comparison.csv"))

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
    parser.add_argument('--taxa_name', type=str, required=True, help='Taxonomic name for analysis')
    parser.add_argument('--taxa_scale', type=str, required=True, help='Taxonomic scale for analysis')
    parser.add_argument('--num_aln', type=int, required=True, help='Number of training loci')
    parser.add_argument('--train_loc_path', type=Path, required=True, help='Path to the training loci directory')
    parser.add_argument('--test_loc_path', type=Path, required=True, help='Path to the testing loci directory')
    parser.add_argument('--taxa_file', type=Path, required=True, help='Path to the reference taxa information file')
    parser.add_argument('--ref_tree', type=Path, required=True, help='Path to the reference tree file')
    parser.add_argument('--model_dir', type=Path, required=True, help='Directory containing initial model files')

    parser.add_argument('-T', '--max_threads', type=str, default="100", help='Maximum number of threads (default: 100)')
    parser.add_argument('-l', '--max_iterate', type=int, default=5, help='Maximum number of iterations (default: 5)')
    parser.add_argument('--converge_thres', type=float, default=0.999, help='Convergence threshold of Q matrix (default: 0.999)')
    parser.add_argument('-p', '--prefix', type=str, default='Q', help='Prefix for output files (default: Q)')

    parser.add_argument('-t', '--test_in_loop', action='store_true', help='Test new estimated model with test data in each loop')
    parser.add_argument('--test_partition', action='store_true', help='Test the final model on partitioned loci')
    parser.add_argument('--fix_subtree_num', action='store_true', help='Fix the number of subtrees during model estimation')
    parser.add_argument('--fix_subtree_topology', action='store_true', help='Fix the topology of subtrees during model estimation')

    parser.add_argument('--tree_size_lower_lim', type=int, default=20, help='Lower limit for the size of subtrees (default: 20)')
    parser.add_argument('--tree_size_upper_lim', type=int, default=100, help='Upper limit for the size of subtrees (default: 100)')  
    parser.add_argument('--prune_mode', type=str, default='random', choices=['random', 'lower', 'upper', 'shallow'], help="Pruning mode (random/lower/upper/shallow) (default: random)")

    parser.add_argument('-c', '--keep_cmd_output', action='store_true', help='Keep detailed command output in the log file')
    parser.add_argument('--keep_tmp', action='store_true', help='Keep temporary files')
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