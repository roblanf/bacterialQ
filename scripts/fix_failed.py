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
from pathlib import Path, PosixPath
from typing import Tuple, Union, List
from Bio import Phylo
 
# Import functional scripts
from Q_convert import *
from grep_iqtree_output import *
from quality_trimming import *
from concat_seq import concatenate_seq_dict, concatenate_seq_list
from get_subtree import prune_tree, remove_redundant_nodes, root_at_outgroups
from mdlogger import *
from metalogger import *
from analyze_best_models import *
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

def run_command(cmd: str, log_file: str, log_any: bool = True, log_output: bool = False, log_time: bool = False, allow_error: bool = False) -> Tuple[str, str, int]:
    """
    Run a shell command, log its output, and return its output and exit code.

    Args:
        cmd (str): Command to run.
        log_file (str): Path to the log file.
        log_any (bool): Whether to log the command itself.
        log_output (bool): Whether to log the command output.
        log_time (bool): Whether to log the command runtime.
        allow_error (bool): Whether to allow the program to continue running even if the command fails.

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
        if not allow_error:
            sys.exit(stderr)

    return stdout, stderr, exit_code

@log_and_handle_error
def sample_alignment(loci_dir: Path, taxa_file_list: Union[Path, List[Path]], output_folder: Path, num_aln: int = None, prop_aln: float = None, combine_taxa_list: bool = False, loci_filter: Path = None, nchar_row = None, nchar_col = None) -> None:
    """
    Sample alignments from the given loci directory and subtree directory.

    Args:
        loci_dir (Path): Path to the directory containing loci alignments.
        taxa_file_list (Union[Path, List[Path]]): Path to the file containing taxa or a list of paths to taxa files.
        output_folder (Path): Path to the sampled alignments output folder.
        num_aln (int, optional): Number of alignments to sample. If both num_aln and prop_aln is None, sample all alignments.
        prop_aln (float, optional): Proportion of alignments to sample. If both num_aln and prop_aln is None, sample all alignments.
        combine_taxa_list (bool): Whether to combine subtrees into a single file.
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

    def process_loci_files(loci_files, taxa_list, output_dir, num_aln=None, prop_aln = None, nchar_row = None, nchar_col = None):
        splited_aln_count, deleted_aln_count = 0, 0
        total_aln_count = len(loci_files)
        if isinstance(taxa_list, Path) and taxa_list.is_file():
            # If a single taxa file is provided
            log_message('process', f"Input a single taxa file: {taxa_list}. Sampling sequences for {len(loci_files)} loci.")
            log_message('result', f"Number of input species: {sum(1 for line in open(taxa_list))}")
            for loci_file in loci_files:
                output_file = output_dir / os.path.basename(loci_file)
                if run_faSomeRecords(loci_file, taxa_list, output_file, nchar_row, nchar_col):
                    splited_aln_count += 1
                else:
                    deleted_aln_count += 1
        elif isinstance(taxa_list, list):
            if combine_taxa_list:
                # If subtrees need to be combined
                log_message('process', f"Input {len(taxa_list)} taxa files and combine them. Sampling sequences for {len(loci_files)} loci.")
                all_taxa_file = output_dir / "combined_taxa.txt"
                with open(all_taxa_file, 'w') as f:
                    for taxa_file in taxa_list:
                        with open(taxa_file, 'r') as tf:
                            content = tf.read()
                            # Check if the content ends with a newline
                            if not content.endswith('\n'):
                                content += '\n'
                            f.write(content)
                target_aln_count = min(num_aln or len(loci_files), len(loci_files))
                for loci_file in loci_files:
                    output_file = output_dir / os.path.basename(loci_file)
                    if run_faSomeRecords(loci_file, all_taxa_file, output_file, nchar_row, nchar_col):
                        splited_aln_count += 1
                    else:
                        deleted_aln_count += 1
                # Remove the combined taxa file to avoid contamination
                os.remove(all_taxa_file)
            else:
                # If subtrees don't need to be combined
                total_aln_count = len(loci_files) * len(taxa_list)
                num_aln = math.ceil(prop_aln * total_aln_count) if prop_aln is not None else num_aln
                log_message('process', f"Input {len(taxa_list)} subtree files and {len(loci_files)} loci files. Total number of potential alignments: {total_aln_count}.")
                if num_aln is not None and num_aln < total_aln_count:
                    # If the requested number of alignments is less than the total potential alignments
                    log_message('result', f"Sub-sampling {num_aln} alignments from {total_aln_count} alignments.")
                    subtree_loci_pairs = list(itertools.product(taxa_list, loci_files))
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
                    for taxa_file in taxa_list:
                        tree_name = os.path.splitext(os.path.basename(taxa_file))[0]
                        for loci_file in loci_files:
                            loci_name = os.path.splitext(os.path.basename(loci_file))[0]
                            ext = os.path.splitext(loci_file)[1]
                            output_file = output_dir / f"{tree_name}_{loci_name}{ext}"
                            if run_faSomeRecords(loci_file, taxa_file, output_file, nchar_row, nchar_col):
                                splited_aln_count += 1
                            else:
                                deleted_aln_count += 1
                    log_message('result', f"Obtained {splited_aln_count} alignments from all potential alignments.")
        else:
            raise ValueError(f"{taxa_list} is neither a file nor a list of files.")

        log_message('process', f"Remaining {splited_aln_count} alignments. Deleted {deleted_aln_count} alignments.")
        return total_aln_count, splited_aln_count

    loci_files = filter_loci_files(loci_dir, loci_filter)

    if not loci_files:
        raise ValueError("Loci set is empty after filtering. Program will terminate.")
    
    total_aln_count, splited_aln_count = process_loci_files(loci_files, taxa_file_list, output_folder, num_aln = num_aln, prop_aln = prop_aln, nchar_row = nchar_row, nchar_col = nchar_col)
    return total_aln_count, splited_aln_count


def get_constraint_tree(loci_dir, subtree_dir, output_tree_path):
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

def time_checkpoint(used_time_list, start_time, time_limit):
    if time_limit is None:
        return False
    end_time = time.time()
    this_round_time = end_time - start_time
    used_time = this_round_time + sum(used_time_list)
    if used_time > time_limit:
        return True
    return False

def bound_next_round_time(times):
    if not times:  # Check if the list is empty
        return 0
    
    min_time = min(times)  # Find the minimum value in the list
    return min_time * 0.6  # Return 0.6 times the minimum value

def fix_best_model_nex(file_path):
    """
    Fix the error that some version of IQ-TREE produces some meaningless command in the .best_model file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    encountered_charpartition = False

    for line in lines:
        if "charpartition mymodels =" in line:
            encountered_charpartition = True
            break
        # Find the last ':' and ';' in the line
        last_colon = line.rfind(':')
        last_semicolon = line.rfind(';')
        if last_colon != -1 and last_semicolon != -1 and last_colon < last_semicolon:
            # Replace the content between the last ':' and the last ';' with a space
            line = line[:last_colon + 1] + ' ' + line[last_semicolon:]
        modified_lines.append(line)

    # Append the remaining lines without modification
    if encountered_charpartition:
        modified_lines.append(line)  # Append the line with 'charpartition mymodels ='
        modified_lines.extend(lines[lines.index(line) + 1:])

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

@log_and_handle_error
def initial_aln_extraction(args: argparse.Namespace) -> Tuple[Path, Path]:
    """
    Extract training and testing loci for all signed species.
    """
    n_species = sum(1 for line in open(args.output_dir / "select_id.txt"))
    nchar_keep_col = max(n_species//100, 4)

    if args.use_outgroup:
        # If outgroup is used, add the outgroup to the taxa list for sampling alignments
        log_message('process', f"Select outgroup taxa for {args.taxa_name}")
        # n_outgroup_taxa = max(min(n_species // 100, max(5, n_species // 100)), 50)
        cmd = f"Rscript get_outgroup.R -t {args.decorated_tree} -n {args.taxa_name} -d 0.1 -o {args.output_dir / 'outgroup_id.txt'} -c {args.taxa_file} -s {args.outgroup_taxa_list} -N 1 --detail"
        run_command(cmd, f"{args.output_dir}/log.md")
        # open the detail file, read and log the first line as the detail of outgroup selection
        with open(args.output_dir / "outgroup_species_info.txt", 'r') as f:
            log_message('result', f"Outgroup selection detail: {f.readline()}")
        taxa_file_list = [args.output_dir / "select_id.txt", args.output_dir / "outgroup_id.txt"]

        # If outgroup is used, sample alignments for the outgroup taxa
        log_message('process', "Abstract alingment of outgroup taxa scale in training set:")
        sample_alignment(args.train_loc_path, taxa_file_list, args.output_dir / "loci" / "training_loci_with_outgroup", num_aln=None, nchar_col=nchar_keep_col, combine_taxa_list=True)
        log_message('process', "Abstract alingment of outgroup taxa scale in testing set:")
        sample_alignment(args.test_loc_path, taxa_file_list, args.output_dir / "loci" / "testing_loci_with_outgroup", num_aln=None, nchar_col=nchar_keep_col, combine_taxa_list=True)

        log_message('process', "Concatenating training loci contains outgroups...")
        concatenate_seq_dict(str(args.output_dir / "loci" / "training_loci_with_outgroup"), str(args.output_dir / "loci" / "concat_training_loci_with_outgroup.faa"))
        log_message('process', "Concatenating testing loci contains outgroups...")
        concatenate_seq_dict(str(args.output_dir / "loci" / "testing_loci_with_outgroup"), str(args.output_dir / "loci" / "concat_testing_loci_with_outgroup.faa"))

    # Sample alignments for the selected taxa
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

def extract_and_log_model_info_concat(iqtree_file):
    """
    Extract model information from the IQ-TREE output file and log it as a Markdown table.

    Args:
        iqtree_file (str): Path to the IQ-TREE output file.

    Returns:
        list: A list of model data containing model name, LogL, and BIC.
    """
    with open(iqtree_file) as f:
        content = f.read()

    model_table_start = content.find("List of models sorted by BIC scores:")
    if model_table_start != -1:
        model_table_end = content.find("AIC, w-AIC", model_table_start) - 1
        model_table = content[model_table_start:model_table_end].strip()

        log_message('result', "Model testing results (concat):")
        log_message('result', "| Model | LogL | BIC |", new_line=True)
        log_message('result', "|-------|------|-----|")

        model_data = []
        for line in model_table.split("\n")[3:]:  # Skip header lines
            if not line.strip():
                continue
            fields = line.split()
            model, logl, bic = fields[0], fields[1], fields[8]
            model_data.append([model, logl, bic])
            log_message('result', f"| {model} | {logl} | {bic} |")

        return model_data
    return []


def extract_and_log_model_info_partition(best_scheme_file, output_dir):
    """
    Extract model information from the partitioned IQ-TREE output file and log it as a Markdown table.

    Args:
        best_scheme_file (Path): Path to the best scheme file of IQ-TREE output.
        output_dir (Path): Output directory for test results.

    Returns:
        dict: A dictionary of model counts.
    """
    model_data = get_and_print_model_counts(best_scheme_file, f"{output_dir}/model_counts.txt")
    best_model_name = max(model_data, key=model_data.get)

    log_message('result', "Best model for test data:")
    log_message('result', best_model_name)

    # Print best models output as a table
    log_message('result', "| Model | Count |", new_line=True)
    log_message('result', "|-------|-------|")

    for model, count in sorted(model_data.items(), key=lambda item: item[1], reverse=True):
        log_message('result', f"| {model} | {count} |")

    return model_data


def test_model(args, output_dir, test_loci_dir, model_name_set, trained_model_nex, mode, loop_id, te=None, initial_tree=None, pre=None, adv_rate_opt=True):
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
        adv_rate_opt (bool, optional): Whether to enable advanced rate models search in IQ-TREE.
    """
    if te:
        initial_tree = None
    if adv_rate_opt:
        model_opt = "TESTNEWONLY"
    else:
        model_opt = "TESTONLY"
    output_dir.mkdir(parents=True, exist_ok=True)
    if mode == "concat":
        if test_loci_dir.is_file():
            concat_test_loci = test_loci_dir
        else:
            # Concatenate test loci into a single alignment
            concat_test_loci = output_dir / "concat_test_loci.faa"
            concatenate_seq_dict(str(test_loci_dir), str(concat_test_loci))
        # Test models on the concatenated alignment
        cmd = f"iqtree -seed 1 -T AUTO -ntmax {args.max_threads} -s {concat_test_loci} -m {model_opt} -mset {model_name_set} -mdef {trained_model_nex} -safe"
    elif mode == "partition":
        # Test models on individual test loci
        cmd = f"iqtree -seed 1 -T AUTO -ntmax {args.max_threads} -p {test_loci_dir} -m {model_opt} -mset {model_name_set} -mdef {trained_model_nex} -safe -wpl"
    else:
        log_message('error', "Invalid name of testing method.")
        return
    if te:
        cmd += f" -te {te}"
    if initial_tree:
        cmd += f" -t {initial_tree} -fast"
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
        model_data = extract_and_log_model_info_concat(test_iqtree_file)
    elif mode == "partition":
        model_data = extract_and_log_model_info_partition(f"{test_prefix}.best_scheme.nex", output_dir)

    return model_data

def compare_trees(args, prev_tree, new_tree, html_output_dir, name):
    cmd_R = f"""
    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '{html_output_dir}', params = list(tree1_path = '{prev_tree}', tree2_path = '{new_tree}', root = FALSE, summary_path = '{args.output_dir}/tree_summary.csv', cophylo_path = '{html_output_dir}/cophylo_plot.pdf', name = '{name}'))"
    """
    
    try:
        run_command(cmd_R, f"{args.output_dir}/log.md", allow_error=True)
        log_link('result', "Tree comparison report", str(Path(html_output_dir) / "tree_comparison.html"))

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

    except subprocess.CalledProcessError as e:
        log_message('error', f"Failed to run command for tree comparison report. Error: {str(e)}")
    except Exception as e:
        log_message('error', f"An unexpected error occurred while generating the tree comparison report. Error: {str(e)}")


def extract_best_bic(model_data):
    """
    Extract the best BIC and corresponding model names for inferred and existed models from the model data.

    Args:
        model_data (list of tuples): Each tuple contains (model, _, bic).

    Returns:
        tuple: (best_inferred_model, best_existed_model, best_inferred_bic, best_existed_bic)
    """
    inferred_bic = float('inf')
    existed_bic = float('inf')
    best_inferred_model = None
    best_existed_model = None
    
    for model, _, bic in model_data:
        bic = float(bic)
        if model.startswith(('d__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__')):
            if bic < inferred_bic:
                inferred_bic = bic
                best_inferred_model = model
        else:
            if bic < existed_bic:
                existed_bic = bic
                best_existed_model = model
    
    return best_inferred_model, best_existed_model, inferred_bic, existed_bic
    
def logging_cross_test_table(ref_concat_result, final_concat_result):
    """
    Log the cross test results as a 3x3 table.
    """

    # Extract best logL for inferred and existed models
    _, _, bic11, bic21 = extract_best_bic(final_concat_result)
    _, _, bic12, bic22 = extract_best_bic(ref_concat_result)
    
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

def reroot_treefile_by_outgroup(tree_file, outgroup_taxa_file, delete_outgroup=True):
    """
    Reroot the tree at the outgroup taxa and delete the outgroup clade, saving the original tree as a backup.

    Args:
        tree_file (str or Path): Path to the original tree file.
        outgroup_taxa_file (str or Path): Path to the file containing outgroup taxa.
        delete_outgroup (bool): Whether to delete the outgroup clade after rerooting. Default is True.
    Returns:
        None
    """
    tree_file = Path(tree_file)
    outgroup_taxa_file = Path(outgroup_taxa_file)
    
    # Add '_with_outgroup' suffix to the original tree file name
    new_tree_with_outgroup = tree_file.with_name(tree_file.stem + '_with_outgroup' + tree_file.suffix)
    
    # Rename the original tree file
    log_message('process', f'Prune outgroup from the tree. The original tree is renamed as {new_tree_with_outgroup}.')
    shutil.move(tree_file, new_tree_with_outgroup)
    
    # Read outgroup taxa from the file
    with open(outgroup_taxa_file, 'r') as file:
        outgroup_list = [line.strip() for line in file.readlines()]
    
    # Root the tree at the outgroups
    root_at_outgroups(new_tree_with_outgroup, outgroup_list, tree_file, delete_outgroup)

def process_directory(dir_path):
    dir = Path(dir_path)

    metafile_path = dir / "meta.json"
    with open(metafile_path, 'r') as f:
        config = json.load(f)
    args = argparse.Namespace(**config)

    metalogger = MetaLogger.get_instance(metafile_path)
    PATH_FASTTREEMP = args.FastTreeMP_path
    initial_model_set = args.initial_model_set

    args.output_dir = Path(args.output_dir)

    setup_logging(args.output_dir, args.verbose)
    files_to_remove = []

    training_loci_path = args.output_dir / "loci" / "training_loci"
    testing_loci_path = args.output_dir / "loci" / "testing_loci"
    concat_training_loci = args.output_dir / "loci" / "concat_training_loci.faa"
    concat_testing_loci = args.output_dir / "loci" / "concat_testing_loci.faa"

    if not args.keep_aln:
        files_to_remove.append(args.output_dir / "loci")
        files_to_remove.append(args.output_dir / "pruned_integrity_table.csv")
    # with open(args.output_dir / "select_id.txt", 'r') as f:
    #     all_species_count = len(f.readlines())

    if args.use_outgroup:
        outgroup_allspc_tree = args.output_dir / "ref_tree_with_outgroups.tre"
    filtered_allspc_tree = args.output_dir / "ref_tree.tre"

    if args.use_outgroup:
        prev_outgroup_tree = outgroup_allspc_tree
        concat_training_loci_og = args.output_dir / "loci" / "concat_training_loci_with_outgroup.faa"
        concat_testing_loci_og = args.output_dir / "loci" / "concat_testing_loci_with_outgroup.faa"

    prev_model = None
    model_set = initial_model_set.replace(" ", "").split(",")


    # Create the directory for the output of models
    models_dir = args.output_dir / "inferred_models"
    # Create the directory for the output of trees
    trees_dir = args.output_dir / "estimated_tree"

    # Final model testing
    final_test_dir = args.output_dir / "final_test"
    final_test_dir.mkdir(parents=True, exist_ok=True)
    final_test_logdir = final_test_dir / "logfiles"
    final_test_logdir.mkdir(exist_ok=True)

    new_tree = final_test_logdir / "best_final_tree.treefile"
    trained_model_nex = models_dir / "trained_model.nex"
    new_model = extract_Q_from_nex(trained_model_nex)[-1]

    concat_all_loci = final_test_dir / "all_loci.faa"
    concatenate_seq_list([concat_training_loci, concat_testing_loci], concat_all_loci)
    all_model_set = f"{initial_model_set},{new_model.model_name}"
    all_trained_model_set = ",".join(list_Q_from_nex(trained_model_nex))
    all_model_set_with_all_trained = f"{initial_model_set},{all_trained_model_set}"
    files_to_remove.append(concat_all_loci)
    if args.use_outgroup:
        concat_all_loci_og = final_test_dir / "all_loci_with_outgroup.faa"
        concatenate_seq_list([concat_training_loci_og, concat_testing_loci_og], concat_all_loci_og)
        files_to_remove.append(concat_all_loci_og)

    best_scheme_file = final_test_logdir / "final_test_partition.best_scheme.nex"
    # 5. Test the final model on partitioned test loci without providing the constraint tree
    if Path(best_scheme_file).exists():
        partition_test_result = extract_and_log_model_info_partition(best_scheme_file, final_test_logdir)
        metalogger.log_parameter("final_test_partition_TR", partition_test_result)
        final_test_partition_info = write_iqtree_statistic(final_test_logdir / "final_test_partition.iqtree", "final_test_partition_TR", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": "Final test", "step": "Final test partition (TR)"})
        metalogger.log_parameter("test_partition_result_TR",final_test_partition_info)
        log_message('process', "### Final model testing on partitioned test loci without constraint tree")
        for root, dirs, files in os.walk(final_test_logdir):
            for file in files:
                if file.startswith('final_test_partition.'):
                    old_path = os.path.join(root, file)
                    new_file = file.replace('final_test_partition', 'final_test_partition_TR', 1)
                    new_path = os.path.join(root, new_file)
                    os.rename(old_path, new_path)
                    print(f'Renamed {old_path} to {new_path}')
    
    new_best_scheme_file = final_test_logdir / "testset_model_partition.best_scheme.nex"
    if not Path(new_best_scheme_file).exists():
        log_message('process', "### Final model testing on partitioned test loci with reference tree as constraint")
        print("Final model testing on partitioned test loci with reference tree as constraint")
        pre_test_part = f"{final_test_logdir}/testset_model_partition"
        cmd = f"iqtree -seed 1 -T 20 -sp {testing_loci_path} -m MF -madd {new_model.model_name} -te {filtered_allspc_tree} -pre {pre_test_part}"
        run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
        final_test_partition_info = write_iqtree_statistic(f"{pre_test_part}.iqtree", "final_test_partition", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": "Final test", "step": "Testset model partition"})
        model_data = extract_and_log_model_info_partition(f"{pre_test_part}.best_scheme.nex", final_test_logdir)
        metalogger.log_parameter("final_test_partition", model_data)
        metalogger.log_parameter("test_partition_result",final_test_partition_info)
        # Re-estimate the tree in concatenated loci using the final model with FastTree
        best_test_model_name =  max(model_data, key=lambda k: model_data[k])
        metalogger.log_parameter("best_test_partition_model", best_test_model_name)
        log_message('process', "Model {best_test_model_name} is selected for final testset tree estimation.")
        if best_test_model_name in all_trained_model_set:
            best_test_model = extract_spc_Q_from_nex(trained_model_nex, best_test_model_name)
        elif best_test_model_name in list_Q_from_nex(args.model_dir):
            best_test_model = extract_spc_Q_from_nex(args.model_dir, best_test_model_name)
        else:
            best_test_model = extract_spc_Q_from_nex(args.model_dir, "LG")
        best_test_model.convert_to_fasttree(final_test_logdir)
        best_test_tree = final_test_logdir / "best_testset_tree.treefile"
        cmd = f"{PATH_FASTTREEMP} -trans {final_test_logdir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/best_testset_tree.log -intree {prev_outgroup_tree} {concat_testing_loci_og} > {best_test_tree}"
        run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
        reroot_treefile_by_outgroup(best_test_tree, args.output_dir / "outgroup_id.txt")
        shutil.copy(best_test_tree, trees_dir / f"FinalModel_FT_Test_G20.treefile")
        metalogger.log_parameter("ll_final_testset_tree", extract_gamma20loglk(f"{final_test_logdir}/best_testset_tree.log"))

        ######### This block is added for the pipeline test, delete in the final version ##########
    # 1. The final concatenated tree (final_concat_tree) obtained using FastTree under concatenated all loci and the final model
    if not "testset_best_model_result" in config:
        # if args.use_outgroup:
        #     cmd = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/final_concat_tree.log -intree {prev_outgroup_tree} {concat_all_loci_og} > {final_test_logdir}/final_concat_tree.treefile"
        # else:
        #     cmd = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/final_concat_tree.log -intree {new_tree} {concat_all_loci} > {final_test_logdir}/final_concat_tree.treefile"
        # run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
        # new_tree = final_test_logdir / "final_concat_tree.treefile"
        # if args.use_outgroup:
        #     reroot_treefile_by_outgroup(new_tree, args.output_dir / "outgroup_id.txt")
        # metalogger.log_parameter("final_concat_tree_ll", extract_gamma20loglk(f"{final_test_logdir}/final_concat_tree.log"))
        # shutil.copy(new_tree, trees_dir / f"FinalModel_FT_All_G20.treefile")
        log_message('process', "### Distinguish best model on concatenated test loci")
        print("Distinguish best model on concatenated test loci")
        testset_best_model_result = test_model(args, final_test_logdir, concat_testing_loci, all_model_set_with_all_trained, trained_model_nex, "concat", loop_id="best_model_test", te = best_test_tree, pre=f"{final_test_logdir}/test_best_concat_model")
        best_infer_str, best_existing_str, best_infer_bic, best_existing_bic = extract_best_bic(testset_best_model_result)
        best_infer_model, best_existing_model = best_infer_str.split('+', 1)[0], best_existing_str.split('+', 1)[0]
        if best_infer_bic < best_existing_bic:
            log_message('result', f"The inferred model {best_infer_model} has better BIC value than the existing model:")
        else:
            log_message('error', f"The existing model {best_existing_model} has better BIC value than the inferred model:")
        log_message('result', "| Type | Best Inferred Model | Best Existing Model |", new_line=True)
        log_message('result', "|------|-----------------|---------------------|")
        log_message('result', f"| Model | {best_infer_str} | {best_existing_str} |")
        log_message('result', f"| BIC | {best_infer_bic} | {best_existing_bic} |")
        metalogger.log_parameters({"best_infer_model_testset":best_infer_str, "best_existing_model_testset":best_existing_str, "best_infer_model_testset_bic":best_infer_bic, "best_existing_model_testset_bic":best_existing_bic})
        metalogger.log_parameter("testset_best_model_result", testset_best_model_result)
        
    ######### This block is added for the pipeline test, delete in the final version ##########

    if not "final_model_verify" in config:
        # 7. Validate the final model in concatenated testing loci
        log_message('process', "### Final model testing of concatenated all loci on final tree")
        print("Final model testing of concatenated all loci on final tree")
        #test version: we use the full concatenated loci for testing instead of test loci
        final_model_verify = test_model(args, final_test_logdir, concat_all_loci, all_model_set, trained_model_nex, "concat", loop_id="final_model_verify", te=new_tree, adv_rate_opt=False, pre=f"{final_test_logdir}/final_model_verify")
        metalogger.log_parameter("final_model_verify", final_model_verify)
        # If the final model has better BIC than the existing models, continue to estimate the final tree on all loci
        best_concat_model = min(final_model_verify, key=lambda x: float(x[2]))  # Find the model with the lowest BIC value

    if True:
        # 7. If the final model is better than the existing models in the concatenated test loci, perform cross-validation
        if args.test_final_tree or args.cross_validation:
            log_message('process', "### Test final tree")
            log_message('process', "#### Final tree estimation on all loci without inferred model")
            if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
                pass
            else:
                if args.use_outgroup:
                    FT_init_tree = prev_outgroup_tree
                    FT_full_aln = concat_all_loci_og
                else:
                    FT_init_tree = new_tree
                    FT_full_aln = concat_all_loci
                cmd = f"{PATH_FASTTREEMP} -wag -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/allloci_wag_tree.log -intree {FT_init_tree} {FT_full_aln} > {final_test_logdir}/allloci_wag_tree.treefile"
                run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                if args.use_outgroup:
                    reroot_treefile_by_outgroup(final_test_logdir / "allloci_wag_tree.treefile", args.output_dir / "outgroup_id.txt")
                shutil.copy(f"{final_test_logdir}/allloci_wag_tree.treefile", trees_dir / f"FT_All_WAG_G20.treefile")
                cmd = f"{PATH_FASTTREEMP} -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/allloci_lg_tree.log -intree {FT_init_tree} {FT_full_aln} > {final_test_logdir}/allloci_lg_tree.treefile"
                run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                if args.use_outgroup:
                    reroot_treefile_by_outgroup(final_test_logdir / "allloci_lg_tree.treefile", args.output_dir / "outgroup_id.txt")
                shutil.copy(f"{final_test_logdir}/allloci_lg_tree.treefile", trees_dir / f"FT_All_LG_G20.treefile")
                wag_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_wag_tree.log")
                lg_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_lg_tree.log")
                existing_tree_ll = max(wag_tree_ll, lg_tree_ll)
                if wag_tree_ll >= lg_tree_ll:
                    existing_model_tree = final_test_logdir / "allloci_wag_tree.treefile"
                    log_message('result', f"WAG model has higher likelihood than LG model, use WAG model for final tree.")
                    metalogger.log_parameter("existing_tree_model", "WAG")
                else:
                    existing_model_tree = final_test_logdir / "allloci_lg_tree.treefile"
                    log_message('result', f"LG model has higher likelihood than WAG model, use LG model for final tree.")
                    metalogger.log_parameter("existing_tree_model", "LG")
    
    log_message('process', "#### Compare final tree with existing model tree")
    print("Compare final tree with existing model tree")
    wag_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_wag_tree.log")
    lg_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_lg_tree.log")
    if wag_tree_ll >= lg_tree_ll:
        existing_model_tree = final_test_logdir / "allloci_wag_tree.treefile"
        metalogger.log_parameter("existing_tree_model", "WAG")
    else:
        existing_model_tree = final_test_logdir / "allloci_lg_tree.treefile"
        metalogger.log_parameter("existing_tree_model", "LG")
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
    metalogger.log_parameter("final_tree_ll", final_tree_ll)
    metalogger.log_parameter("existing_tree_ll", existing_tree_ll)
    
    existing_tree_ll = max(wag_tree_ll, lg_tree_ll)
    final_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/best_final_tree.log")
    if final_tree_ll <= existing_tree_ll:
        log_message('error', "The final model tree does not have better likelihood than the existing model tree.")
        best_concat_tree = existing_model_tree
    else:
        log_message('process', "The final model tree has better likelihood than the existing model tree.")
        best_concat_tree = new_tree
            
    if not "concat_best_model_result" in config:
        log_message('process', "### Distinguish best model on final tree in concatenated all loci")
        concat_best_model_result = test_model(args, final_test_logdir, concat_all_loci, all_model_set_with_all_trained, trained_model_nex, "concat", loop_id="best_model_concat", te = best_concat_tree, pre=f"{final_test_logdir}/allloci_best_concat_model")
        best_infer_str, best_existing_str, best_infer_bic, best_existing_bic = extract_best_bic(concat_best_model_result)
        best_infer_model, best_existing_model = best_infer_str.split('+', 1)[0], best_existing_str.split('+', 1)[0]
        if best_infer_bic < best_existing_bic:
            log_message('result', f"The inferred model {best_infer_model} has better BIC value than the existing model:")
        else:
            log_message('error', f"The existing model {best_existing_model} has better BIC value than the inferred model:")
        log_message('result', "| Type | Best Inferred Model | Best Existing Model |", new_line=True)
        log_message('result', "|------|-----------------|---------------------|")
        log_message('result', f"| Model | {best_infer_str} | {best_existing_str} |")
        log_message('result', f"| BIC | {best_infer_bic} | {best_existing_bic} |")
        metalogger.log_parameters({"best_infer_model_concat":best_infer_str, "best_existing_model_concat":best_existing_str, "best_infer_model_concat_bic":best_infer_bic, "best_existing_model_concat_bic":best_existing_bic})
        metalogger.log_parameter("concat_best_model_result", concat_best_model_result)

    # 8. Plot RF and nRF distance among estimated trees and reference tree
    cmd = f"Rscript ./analysis/write_pairwise_tree_dist.R {trees_dir}"
    run_command(cmd, f"{args.output_dir}/log.md", log_any=False, allow_error=True)
    log_link('result', "Heatmap of RF distance of trees:", str(trees_dir / "RF_dist.png"))
    log_link('result', "Heatmap of nRF distance of trees:", str(trees_dir / "nRF_dist.png"))
    log_link('result', "Pairwise tree distance metrics: ", str(trees_dir / "tree_pairwise_compare.csv"))

    # 9. Generate summary for final test
    log_message('process', "### Record files")
    log_link('result', "Summary of IQ-TREE result", str(args.output_dir / "iqtree_results.csv"))
    log_link('result', "Summary of tree comparison", str(args.output_dir / "tree_summary.csv"))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a directory based on the existence of a specific file.")
    parser.add_argument("directory", type=str, help="The directory to check")

    arg_fix = parser.parse_args()

    while True:
        dir_to_check = Path(arg_fix.directory)
        process_directory(dir_to_check)