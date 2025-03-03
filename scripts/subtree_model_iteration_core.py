#!/usr/bin/env python3
# The only difference of this version is replace the input with taxa_scale--taxa_name with the input of taxa_list file.
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
from fasta_filter import *

# Define constants
keep_model_thres = 0.05
model_test_reduced_set = "LG,WAG,Q.PFAM,JTT,DCMUT,PMB,Q.YEAST,Q.INSECT,Q.PLANT,Q.MAMMAL,Q.BIRD,CPREV,MTMET,MTINV,MTVER"

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
                subtree_name = re.search(r'subtree_\d+', file).group()
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
        modified_lines.append(line)
        modified_lines.extend(lines[lines.index(line) + 1:])

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

@log_and_handle_error
def initial_aln_extraction(args: argparse.Namespace) -> Tuple[Path, Path]:
    """
    Extract loci for all signed species.
    """
    n_species = sum(1 for line in open(args.taxa_list))
    nchar_keep_col = max(n_species//100, 4)

    log_message('process', "Abstract alignment of selected taxa scale:")
    sample_alignment(args.loci_path, args.taxa_list, args.output_dir / "loci" / "loci", num_aln=None, nchar_col=nchar_keep_col)
    # For all the loci, apply the secondary quality filter to remove low-quality sites
    log_message('process', "Secondary quality trimming of loci:")
    for loci_file in (args.output_dir / "loci" / "loci").glob("*.fa"):
        aln = fasta_to_array(loci_file)
        aln.filter_array_with_ratio(0, args.integrity_filter)
        aln.filter_array_with_nstatus(args.nstatus_filter)
        aln.array_to_fasta(loci_file)
    
    concat_loci = args.output_dir / "loci" / "concat_loci.faa"
    log_message('process', "Concatenating loci...")
    concatenate_seq_dict(str(args.output_dir / "loci" / "loci"), str(concat_loci))
    
    if args.use_outgroup:
        taxa_file_list = [args.taxa_list, args.outgroup_taxa_list]
 
        log_message('process', "Abstract alignment of outgroup taxa scale:")
        sample_alignment(args.loci_path, taxa_file_list, args.output_dir / "loci" / "loci_with_outgroup", num_aln=None, nchar_col=nchar_keep_col, combine_taxa_list=True)
        log_message('process', "Concatenating loci contains outgroups...")
        concatenate_seq_dict(str(args.output_dir / "loci" / "loci_with_outgroup"), str(args.output_dir / "loci" / "concat_loci_with_outgroup.faa"))
        

def prune_subtrees(args, ref_tree, subtree_dir, num_subtrees, prune_mode):
    """
    Prune subtrees from the filtered all-species tree.

    Args:
        args (argparse.Namespace): Command line arguments.
        ref_tree (Path): Path to the reference tree file.
        subtree_dir (Path): Directory for the current iteration's subtrees.
        num_subtrees (int, optional): Number of subtrees to prune. If None, prune all subtrees.
        prune_mode (str): Pruning mode (split/lower/upper/deep).
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
        model_opt = "TESTNEWONLY -cmin 5 -cmax 8"
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
        step = re.split(r'/', pre)[-1]
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
    Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '{html_output_dir}', params = list(tree1_path = '{prev_tree}', tree2_path = '{new_tree}', summary_path = '{args.output_dir}/tree_summary.csv', cophylo_path = '{html_output_dir}/cophylo_plot.pdf', name = '{name}'))"
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

        return nrf_dist

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
        if model.startswith(('d__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__', "Q.")):
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


def main(args: argparse.Namespace) -> None:
    """
    Main function to run the model estimation pipeline.

    Args:
        args (argparse.Namespace): Command line arguments.
    """
    PATH_FASTTREEMP = args.FastTreeMP_path
    initial_model_set = args.initial_model_set
    global keep_model_thres

    setup_logging(args.output_dir, args.verbose)
    files_to_remove = []
    num_aln_inloop = []
    total_aln_inloop = []
    time_usage_inloop = []
    training_tree_ll = []
    Q_coef_inloop = []
    Q_dist_inloop = []
    inloop_nRF_dist = []

    log_message('process', "## Initialization")
    log_message('result', f"Running model estimation with the following parameters:")
    log_message('result', f"  Maximum iterations: {args.max_iterate}")
    log_message('result', f"  Convergence threshold: {args.t_model_converge}")
    log_message('result', f"  File prefix: {args.prefix}")
    log_message('result', f"  Number of alignment for inferring model: {args.num_aln}")
    log_message('result', f"  Drop species threshold: {args.t_drop_species}")
    log_message('result', f"  Drop locus threshold: {args.t_drop_loc}")
    log_message('result', f"  Initial model set: {initial_model_set}")
    log_message('result', f"  Keep model threshold: {keep_model_thres}")
    log_message('result', f"  Pruning mode: {args.prune_mode}")
    log_message('result', f"  Lower limit for subtree size: {args.tree_size_lower_lim}")
    log_message('result', f"  Upper limit for subtree size: {args.tree_size_upper_lim}")

    log_message('process', "### Initial data extraction")
    initial_aln_extraction(args)
    concat_loci = args.output_dir / "loci" / "concat_loci.faa"
    if args.use_outgroup:
        concat_loci_og = args.output_dir / "loci" / "concat_loci_with_outgroup.faa"
    loci_path = args.output_dir / "loci" / "loci"
    if not args.keep_aln:
        files_to_remove.append(args.output_dir / "loci")
        files_to_remove.append(args.output_dir / "pruned_integrity_table.csv")

    log_message('process', "### Prune reference tree")
    prune_tree(args.ref_tree, [args.taxa_list], args.output_dir / "ref_tree.tre")
    if args.use_outgroup:
        prune_tree(args.ref_tree, [args.taxa_list, args.outgroup_taxa_list], args.output_dir / "ref_tree_with_outgroups.tre")
        outgroup_allspc_tree = args.output_dir / "ref_tree_with_outgroups.tre"
    filtered_allspc_tree = args.output_dir / "ref_tree.tre"

    iteration_id = 1
    prev_model = None
    model_set = initial_model_set.replace(" ", "").split(",")
    trained_model_nex = None
    prev_tree = filtered_allspc_tree
    initial_best_model_name = None
    new_model = None
    if args.use_outgroup:
        prev_outgroup_tree = outgroup_allspc_tree
        concat_loci_og = args.output_dir / "loci" / "concat_loci_with_outgroup.faa"

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
           num_subtrees = math.ceil(args.num_aln * 1.0 / len(list(args.output_dir.glob('loci/loci/*.fa*'))))
        else:
            num_subtrees = None
        prune_subtrees(args, prev_tree, subtree_dir, num_subtrees, args.prune_mode)

        log_message('process', "### Extract subtree loci for training model")
        taxa_files = list((subtree_dir / "taxa_list").glob("*.txt"))
        total_aln, num_aln = sample_alignment(loci_path, taxa_files, iteration_dir / "training_loci", num_aln=args.num_aln, nchar_row = 3, nchar_col = 1)
        num_aln_inloop.append(num_aln)
        total_aln_inloop.append(total_aln)
        subtree_train_loci_dir = iteration_dir / "training_loci"
        files_to_remove.append(subtree_train_loci_dir)

        # 3. Run ModelFinder to find the best model using the pruned subtrees
        log_message('process', "### Subtree update")
        subtree_update_dir = iteration_dir / "subtree_update"
        subtree_update_dir.mkdir(parents=True, exist_ok=True)
        num_threads = min(int(args.max_threads), len(list(subtree_train_loci_dir.glob("*.fa*"))))
        model_set_str = ",".join(model_set)
        cmd = f"iqtree -seed 1 -T {num_threads} -S {subtree_train_loci_dir} -m MFP -mset {model_set_str}"
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

        subtree_model_nex = subtree_update_dir / f"{args.prefix}.best_model.nex"
        subtree_iqtree_path = subtree_update_dir / f"{args.prefix}.iqtree"  
        subtree_update_trees = subtree_update_dir / f"{args.prefix}.treefile" 
        write_iqtree_statistic(subtree_iqtree_path, f"{args.prefix}", f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": iteration_id, "step": "subtree_update"})
        plot_loci_statistic(subtree_iqtree_path, subtree_update_dir / "loci_statistic.png")
        log_link('result', "Subtree update log", str(subtree_update_dir / f"{args.prefix}.iqtree"))

        # Detele reduandant comma in best_model nex file
        fix_best_model_nex(subtree_model_nex)

        # Get the initial best model name
        subtree_model_data = get_and_print_model_counts(subtree_model_nex, f"{subtree_update_dir}/model_count.txt")
        best_model_name = max(subtree_model_data, key=subtree_model_data.get)
        if iteration_id == 1:
            initial_best_model_name = best_model_name
        log_message('result', f"Best models for iteration {iteration_id}:")
        log_message('result', best_model_name)

        # Print best models output as a table
        log_message('result', "| Model | Count |", new_line = True)
        log_message('result', "|-------|-------|")
        for model, count in sorted(subtree_model_data.items(), key=lambda item: item[1], reverse=True):
            log_message('result', f"| {model} | {count} |")
        
        # Set prev_model to the best model of past iteration
        if best_model_name in initial_model_set:
            prev_model = extract_spc_Q_from_nex(args.model_dir, best_model_name)
        else:
            prev_model = extract_spc_Q_from_nex(trained_model_nex, best_model_name)

        # Update model_set based on the best models
        best_models_output = subtree_update_dir / 'model_count.txt'
        with open(best_models_output) as f:
            best_model_counts = {}
            for line in f:
                line = line.strip()
                if line:
                    count, model = line.split()
                    best_model_counts[model] = int(count)
        
        if new_model:
            del best_model_counts[new_model.model_name]
            keep_model_thres = 0.1
        total_models = sum(best_model_counts.values())
        model_set = [model for model, count in best_model_counts.items() if count / total_models >= keep_model_thres]

        # Check the time usage before the next step
        if args.time_limit:
            if time_checkpoint(time_usage_inloop, loop_start_time, args.time_limit):
                log_message('error', f"Time limit reached. Program will(should) terminate in loop {iteration_id} before model update.")
                if iteration_id > 1:
                    break

        # 4. Estimate new models using ModelFinder based on the best model for each partition and the pruned subtree
        log_message('process', "### Model update")
        model_update_dir = iteration_dir / "model_update"
        model_update_dir.mkdir(parents=True, exist_ok=True)
        if not trained_model_nex:
            cmd = f"iqtree -seed 1 -T {num_threads} -S {subtree_model_nex} -te {subtree_update_trees} --model-joint GTR20+FO --init-model {best_model_name} -pre {model_update_dir / args.prefix}"  
        else:
            cmd = f"iqtree -seed 1 -T {num_threads} -S {subtree_model_nex} -te {subtree_update_trees} --model-joint GTR20+FO --init-model {best_model_name} -mdef {trained_model_nex} -pre {model_update_dir / args.prefix}"
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
        model_set.append(new_model.model_name)
        model_set_str = ",".join(model_set)

        log_link('result', "New model", str(models_dir / f"{new_model.model_name}"))
        log_message('result', f"Model set for next iteration: {model_set_str}")

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
            try:
                run_command(cmd, f"{args.output_dir}/log.md", log_any=False)
                log_message('result', "Generated summary for model update, see" + str(summary_dir))
            except Exception as e:
                log_message('error', f"Failed to run command for generate model update summary. Error: {str(e)}")

        # 5. Check for model convergence
        log_message('process', "### Check model convergence")
        log_message('process', f"Iteration {iteration_id}: Checking convergence")
        ifconverge, corr, dist = prev_model.check_convergence(new_model, threshold=args.t_model_converge)
        log_message('result', f"Pearson's correlation: {corr}")  
        log_message('result', f"Euclidean distance: {dist}")
        Q_coef_inloop.append(corr)
        Q_dist_inloop.append(dist)

        if ifconverge:
            # If convergence is reached, stop the iteration
            log_message('result', f"Convergence of model reached at iteration {iteration_id}")
            loop_end_time = time.time()
            loop_time = loop_end_time - loop_start_time
            time_usage_inloop.append(loop_time)
            break
        
        # 6. Re-estimate the tree using FastTree on the concatenated loci
        log_message('process', "### Tree update")
        tree_update_dir = iteration_dir / "tree_update"
        tree_update_dir.mkdir(parents=True, exist_ok=True)

        # Set the number of threads for fasttree to 3
        os.environ['OMP_NUM_THREADS'] = '3'
        if args.use_outgroup:
            cmd_FT = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {tree_update_dir}/fasttree.log -intree {prev_outgroup_tree} {concat_loci_og} > {tree_update_dir / args.prefix}_{iteration_id}.treefile"
        else:
            cmd_FT = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {tree_update_dir}/fasttree.log -intree {prev_tree} {concat_loci} > {tree_update_dir / args.prefix}_{iteration_id}.treefile"
        run_command(cmd_FT, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)

        log_link('result', "FastTree log", str(tree_update_dir / "fasttree.log"))
        new_tree = tree_update_dir / f"{args.prefix}_{iteration_id}.treefile"
        training_tree_ll.append(extract_gamma20loglk(f"{tree_update_dir}/fasttree.log"))
        if args.use_outgroup:
            reroot_treefile_by_outgroup(new_tree, args.outgroup_taxa_list)
            prev_outgroup_tree = new_tree.with_name(new_tree.stem + '_with_outgroup' + new_tree.suffix)
   
        shutil.copy(new_tree, trees_dir / f"Loop_{iteration_id}_FT_Train_G20.treefile")
        nrf_dist = compare_trees(args, prev_tree, new_tree, iteration_dir, f"loop_{iteration_id}")
        inloop_nRF_dist.append(nrf_dist)

        prev_model = new_model
        prev_tree = new_tree

        loop_end_time = time.time()
        loop_time = loop_end_time - loop_start_time
        time_usage_inloop.append(loop_time)
        log_message('process', f"Time usage for Loop_{iteration_id}: {loop_time:.2f} seconds ({loop_time/3600:.2f} h)")

        # Check for tree convergence
        if nrf_dist < args.t_tree_converge:
            log_message('result', f"Convergence of tree reached at iteration {iteration_id} (nRF distance: {nrf_dist})")
            break

        # Check the time usage before the next step
        if args.time_limit:
            if (sum(time_usage_inloop) > args.time_limit):
                log_message('process', f"Time limit reached. Program will terminate in the end of loop {iteration_id}.")
                break
    
            if (sum(time_usage_inloop) + bound_next_round_time(time_usage_inloop) > args.time_limit):
                log_message('process', f"The estimated remaining time is insufficient to complete the next iteration. Program will terminate in the end of loop {iteration_id}.")
                break 

        if iteration_id >= args.max_iterate:
            # If the maximum number of iterations is reached, stop the iteration
            log_message('process', f"Stop loop after {args.max_iterate} times of iteration")
            break
        
        time_usage_inloop.append(loop_time)
        iteration_id += 1
    
    # record parameters
    metalogger.log_parameters({"num_aln_inloop": num_aln_inloop, "total_aln_inloop": total_aln_inloop, 
                               "time_usage_inloop": time_usage_inloop, "training_tree_ll": training_tree_ll, 
                               "Q_coef_inloop": Q_coef_inloop, "Q_dist_inloop": Q_dist_inloop, 
                               "inloop_nRF_dist": inloop_nRF_dist})

    # Final model testing
    log_message('process', "## Final test", new_line = True)
    final_test_dir = args.output_dir / "final_test"
    final_test_dir.mkdir(parents=True, exist_ok=True)
    final_test_logdir = final_test_dir / "logfiles"
    final_test_logdir.mkdir(exist_ok=True)
    
    all_model_set = f"{model_test_reduced_set},{new_model.model_name}"
    all_trained_model_set = ",".join(list_Q_from_nex(trained_model_nex))
    all_model_set_with_all_trained = f"{model_test_reduced_set},{all_trained_model_set}"
    if args.use_outgroup:
        FT_init_tree = prev_outgroup_tree
        FT_full_aln = concat_loci_og
    else:
        FT_init_tree = new_tree
    
    # 1. Estimate the best final tree on the concatenated loci
    if args.estimate_best_final_tree or args.test_final_tree or args.cross_validation:
        log_message('process', "### Final tree estimation on all loci")
        if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
            cmd = f"iqtree -seed 1 -T AUTO -ntmax {num_threads} -p {loci_path} -t {new_tree} -m MFP -mset {all_model_set} -mdef {trained_model_nex} -pre {final_test_logdir}/best_final_tree -wpl -safe"
            if args.final_tree_tool == "IQ":
                cmd += " -B 1000"
            if args.final_tree_tool == "IQFAST":
                cmd += " -fast" 
        else:
            if args.use_outgroup:
                cmd = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/best_final_tree.log -intree {prev_outgroup_tree} {concat_loci_og} > {final_test_logdir}/best_final_tree.treefile"
            else:
                cmd = f"{PATH_FASTTREEMP} -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/best_final_tree.log -intree {new_tree} {concat_loci} > {final_test_logdir}/best_final_tree.treefile"
        run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
        new_tree = final_test_logdir / "best_final_tree.treefile"
        if args.use_outgroup:
            reroot_treefile_by_outgroup(new_tree, args.outgroup_taxa_list)

        if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
            final_tree_info = write_iqtree_statistic(f"{final_test_logdir}/best_final_tree.iqtree" ,args.prefix , f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": "Final test", "step": "Final best tree"})
            final_partition_result = extract_and_log_model_info_partition(f"{final_test_logdir}/best_final_tree.best_scheme.nex", f"{final_test_logdir}/final_partition_tree_models.txt")
            metalogger.log_parameter("final_partition_result", final_partition_result)
            metalogger.log_parameter("final_tree_info", final_tree_info)
            shutil.copy(new_tree, trees_dir / f"FinalModel_IQ_All_partition.treefile")
        else:
            metalogger.log_parameter("final_tree_ll", extract_gamma20loglk(f"{final_test_logdir}/best_final_tree.log"))
            shutil.copy(new_tree, trees_dir / f"FinalModel_FT_All_G20.treefile")
    
    # 2. Compare the final tree with the reference tree
    log_message('process', "### Tree comparison")
    log_message('result', "Compare the final tree with reference tree:")
    compare_trees(args, filtered_allspc_tree, new_tree, args.output_dir, "final_tree_compare")

    # 3. PCA plot for all existing models with final trained model
    log_message('process', "### PCA Plot for all models")
    cmd = f"Rscript PCA_Q.R {args.model_dir} {models_dir}/trained_model.nex {models_dir}"
    run_command(cmd, f"{args.output_dir}/log.md", allow_error=True)
    log_link('result', "PCA plot of Q matrultices", str(models_dir / "PCA_Q.png"))
    log_link('result', "PCA plot of state frequencies", str(models_dir / "PCA_F.png"))

    # Option: Validate the final model in subtrees on testing loci
    if args.test_subtrees:
        log_message('process', "### Final model testing of test loci in subtrees")
        log_message('process', "#### Extract subtree loci for testing")
        subtree_test_loci_dir = final_test_logdir / "subtree_test_alignment"
        files_to_remove.append(subtree_test_loci_dir)
        prune_subtrees(args, new_tree, final_test_logdir / "subtrees", num_subtrees=None, prune_mode="split")
        taxa_files_test = list((final_test_logdir / "subtrees" / "taxa_list").glob("*.txt"))
        sample_alignment(loci_path, taxa_files_test, subtree_test_loci_dir, nchar_row=3, nchar_col=1)
        log_message('process', "#### Test model performance on subtrees")
        test_model(args, final_test_logdir, subtree_test_loci_dir, model_set_str, trained_model_nex, "partition", loop_id="final_test_subtrees", te=None, adv_rate_opt=False, pre=f"{final_test_logdir}/test_in_subtree")
            
    # 4. Re-verify the best model on the concatenated loci with reference tree as topology constraint
    log_message('process', "### Test model on reference tree in concatenated loci")
    concat_best_model_result = test_model(args, final_test_logdir, concat_loci, all_model_set_with_all_trained, trained_model_nex, "concat", loop_id="best_model_reftree", te = filtered_allspc_tree, pre=f"{final_test_logdir}/reftree_best_concat_model", adv_rate_opt=True)
    metalogger.log_parameter("concat_best_model_result", concat_best_model_result)
    best_infer_str, best_existing_str, best_infer_bic, best_existing_bic = extract_best_bic(concat_best_model_result)
    metalogger.log_parameters({"best_infer_model_concat":best_infer_str, "best_existing_model_concat":best_existing_str, "best_infer_model_concat_bic":best_infer_bic, "best_existing_model_concat_bic":best_existing_bic})
    best_infer_model, best_existing_model = best_infer_str.split('+', 1)[0], best_existing_str.split('+', 1)[0]
    if best_infer_bic < best_existing_bic:
        log_message('result', f"The inferred model {best_infer_model} has better BIC value than the existing model:")
    else:
        log_message('error', f"The existing model {best_existing_model} has better BIC value than the inferred model:")
        log_message('process', "Skip following tests.")
    log_message('result', "| Type | Best Inferred Model | Best Existing Model |", new_line=True)
    log_message('result', "|------|-----------------|---------------------|")
    log_message('result', f"| Model | {best_infer_str} | {best_existing_str} |")
    log_message('result', f"| BIC | {best_infer_bic} | {best_existing_bic} |")

    if best_infer_bic < best_existing_bic:
        # 5. If the final model is better than the existing models in the concatenated test loci, perform final tree test or cross-validation
        if args.test_final_tree or args.cross_validation:
            log_message('process', "### Test final tree")
            log_message('process', "#### Final tree estimation on all loci without inferred model")
            if args.final_tree_tool == "IQ" or args.final_tree_tool == "IQFAST":
                existing_model_tree = final_test_logdir / "existing_model_tree.treefile"
                cmd = f"iqtree -seed 1 -T AUTO -ntmax {num_threads} -p {loci_path} -t {new_tree} -m MFP -mset {initial_model_set} -pre {final_test_logdir}/existing_model_tree -wpl -safe"
                if args.final_tree_tool == "IQ":
                     cmd += " -B 1000" 
                if args.final_tree_tool == "IQFAST":
                    cmd += " -fast"
                run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                shutil.copy(existing_model_tree, trees_dir / f"ExistModel_IQ_All_partition.treefile")
                existing_tree_info = write_iqtree_statistic(f"{final_test_logdir}/existing_model_tree.iqtree", args.prefix, f"{args.output_dir}/iqtree_results.csv", extra_info={"loop": "Final test", "step": "Existing model tree"})
                model_select_result = extract_and_log_model_info_partition(f"{final_test_logdir}/existing_model_tree.best_scheme.nex", f"{final_test_logdir}/existing_model_tree_models.txt")
                metalogger.log_parameter("existing_model_tree_models", model_select_result)
                best_existing_model = max(model_select_result, key=model_select_result.get)
            else:
                if args.use_outgroup:
                    FT_init_tree = prev_outgroup_tree
                    FT_full_aln = concat_loci_og
                else:
                    FT_init_tree = new_tree
                    FT_full_aln = concat_loci
                
                if not best_existing_model == "LG":
                    extract_spc_Q_from_nex(args.model_dir, best_existing_model).convert_to_fasttree(final_test_logdir)
                    cmd = f"{PATH_FASTTREEMP} -trans {final_test_logdir}/Q_matrix_fasttree.txt -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/allloci_best_existing_model_tree.log -intree {FT_init_tree} {FT_full_aln} > {final_test_logdir}/allloci_best_existing_model_tree.treefile"
                    run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                    if args.use_outgroup:
                        reroot_treefile_by_outgroup(final_test_logdir / "allloci_best_existing_model_tree.treefile", args.outgroup_taxa_list)
                    shutil.copy(f"{final_test_logdir}/allloci_best_existing_model_tree.treefile", trees_dir / f"FT_All_Best_Existing_Model_G20.treefile")
                    best_model_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_best_existing_model_tree.log")
                cmd = f"{PATH_FASTTREEMP} -lg -gamma -spr 4 -sprlength 1000 -boot 100 -log {final_test_logdir}/allloci_lg_tree.log -intree {FT_init_tree} {FT_full_aln} > {final_test_logdir}/allloci_lg_tree.treefile"
                run_command(cmd, f"{args.output_dir}/log.md", log_output=args.keep_cmd_output, log_time=True)
                if args.use_outgroup:
                    reroot_treefile_by_outgroup(final_test_logdir / "allloci_lg_tree.treefile", args.outgroup_taxa_list)
                shutil.copy(f"{final_test_logdir}/allloci_lg_tree.treefile", trees_dir / f"FT_All_LG_G20.treefile")
                lg_tree_ll = extract_gamma20loglk(f"{final_test_logdir}/allloci_lg_tree.log")
                if best_existing_model == "LG":
                    best_model_tree_ll = lg_tree_ll
                if best_model_tree_ll > lg_tree_ll:
                    existing_model_tree = final_test_logdir / "allloci_best_existing_model_tree.treefile"
                    log_message('result', f"{best_existing_model} model has higher likelihood than LG model, use best_existing_model model for final tree.")
                    metalogger.log_parameter("existing_tree_model", best_existing_model)
                else:
                    existing_model_tree = final_test_logdir / "allloci_lg_tree.treefile"
                    log_message('result', f"LG model has higher likelihood than {best_existing_model} model, use LG model for final tree.")
                    metalogger.log_parameter("existing_tree_model", "LG")
                existing_tree_ll = max(best_model_tree_ll, lg_tree_ll)

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
            metalogger.log_parameters({"final_tree_ll":final_tree_ll, "existing_tree_ll":existing_tree_ll})

            if final_tree_ll <= existing_tree_ll:
                log_message('error', "The final model tree does not have better likelihood than the existing model tree.")
                best_concat_tree = existing_model_tree
                # If the final model has better BIC than the existing models, re-estimate the best model on the best tree
                log_message('process', "### Distinguish best trained model on best concatenated tree")
                best_trained_model_result = test_model(args, final_test_logdir, concat_loci, all_trained_model_set, trained_model_nex, "concat", loop_id="best_trained_model", te = best_concat_tree, pre=f"{final_test_logdir}/concat_best_trained_model", adv_rate_opt=True)
                metalogger.log_parameter("best_trained_model_concat", best_trained_model_result)
                # If the final model has better BIC than the existing models, continue to estimate the final tree on all loci
                best_trained_model_str = min(best_trained_model_result, key=lambda x: float(x[2])).split('+', 1)[0]  # Find the best trained model with the lowest BIC value
                log_message('result', f"Best trained model on the best concatenated tree: {best_trained_model_str}")
                metalogger.log_parameter("best_trained_model", best_trained_model_str)
            else:
                log_message('process', "The final model tree has better likelihood than the existing model tree.")
                best_concat_tree = new_tree
            # If the final model has better LogL, carry out cross-validation
            if args.cross_validation:
                # Use a temporary directory to store the results of the reference tree test
                cross_validation_dir = final_test_dir / "cross_validation"
                cross_validation_dir.mkdir(parents=True, exist_ok=True)
                log_message('process', "### Cross validation")
                log_message('process', "#### All models testing on existing model tree and all loci")
                existing_model_tree_result = test_model(args, cross_validation_dir, concat_loci, all_model_set, trained_model_nex, "concat", loop_id="cross_existing_model_tree", te=existing_model_tree, pre=f"{cross_validation_dir}/cross_existing_model_tree")
                # Compare the results of the two tests
                log_message('process', "#### All models testing on final best tree and all loci")
                inferred_model_tree_result = test_model(args, cross_validation_dir, concat_loci, all_model_set, trained_model_nex, "concat", loop_id="cross_final_tree", te=new_tree, pre=f"{cross_validation_dir}/cross_final_tree")
                logging_cross_test_table(existing_model_tree_result, inferred_model_tree_result)

    # 5. Compare the final model with the best existing model
    if best_existing_model:
        log_message('process', "### Model comparison")
        best_existing_model = extract_spc_Q_from_nex(args.model_dir, best_existing_model)
        ifconverge, corr, dist = best_existing_model.check_convergence(new_model, threshold=args.t_model_converge)
        log_message('result', f"Comparison between best existing model ({best_existing_model.model_name}) and final model ({new_model.model_name}):")
        log_message('result', f"Pearson's correlation: {corr}")  
        log_message('result', f"Euclidean distance: {dist}")  
        bubble_plot(best_existing_model, final_test_dir / "best_existing_model.png")
        log_link('result', "Best existing model bubble plot", str(final_test_dir / "best_existing_model.png"))
        bubble_plot(new_model, final_test_dir / "final_model.png")
        log_link('result', "Final model bubble plot", str(final_test_dir / "final_model.png"))
        bubble_difference_plot(best_existing_model, new_model, final_test_dir / "model_comparison.png")
        log_link('result', "Model comparison plot", str(final_test_dir / "model_comparison.png"))

    # 6. Plot RF and nRF distance among estimated trees and reference tree
    log_message('process', "### Pairwise tree distance comparison")
    cmd = f"Rscript ./analysis/write_pairwise_tree_dist.R {trees_dir}"
    run_command(cmd, f"{args.output_dir}/log.md", log_any=False, allow_error=True)
    log_link('result', "Heatmap of RF distance of trees:", str(trees_dir / "RF_heatmap.png"))
    log_link('result', "Heatmap of nRF distance of trees:", str(trees_dir / "nRF_heatmap.png"))
    log_link('result', "Pairwise tree distance metrics: ", str(trees_dir / "tree_pairwise_compare.csv"))

    # 7. Generate record for IQ-TREE and tree compare
    log_message('process', "### Record files")
    log_link('result', "Record of IQ-TREE result", str(args.output_dir / "iqtree_results.csv"))
    log_link('result', "Record of tree comparison", str(args.output_dir / "tree_summary.csv"))

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
    #test version: Add prop_aln option for better select the number of alignment for model estimation
    # Create a mutually exclusive group for num_aln and prop_aln
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-N', '--num_aln', type=int, help='Number of alignments to sample')
    parser.add_argument('-n', '--taxa_list', type=str, required=True, help='Taxa list for analysis')
    parser.add_argument('-a', '--loci_path', type=Path, required=True, help='Path to the loci directory')
    parser.add_argument('-r', '--ref_tree', type=Path, required=True, help='Path to the reference tree file')
    parser.add_argument('-m', '--model_dir', type=Path, required=True, help='Directory containing initial model files')
    parser.add_argument('-M', '--initial_model_set', type=str, default="LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV", help='Initial model set for ModelFinder (default: LG,Q.PFAM,JTT,WAG,Q.YEAST,Q.PLANT,Q.MAMMAL,CPREV)')
    parser.add_argument('--t_drop_species', type=float, default=0.2, help='Threshold of sequence integrity for dropping species (default: 0.2)')
    parser.add_argument('--t_drop_loc', type=float, default=0.1, help='Threshold of sequence integrity for dropping loci (default: 0.1)')

    parser.add_argument('-T', '--max_threads', type=str, default="100", help='Maximum number of threads (default: 100)')
    parser.add_argument('-l', '--max_iterate', type=int, default=5, help='Maximum number of iterations (default: 5)')
    parser.add_argument('-V', '--t_model_converge', type=float, default=0.999, help='Convergence threshold of Q matrix (default: 0.999)')
    parser.add_argument('--t_tree_converge', type=float, default=0.005, help='Convergence threshold of nRF distance for tree estimation (default: 0.005)')
    parser.add_argument('--time_limit', type=int, default=None, help='Time limit (seconds) inner model inference stage (default: None)')
    parser.add_argument('-p', '--prefix', type=str, default='Q', help='Prefix for output files (default: Q)')

    parser.add_argument('--test_subtrees', action='store_true', help='Test the final model on test loci in subtrees')
    parser.add_argument('--estimate_best_final_tree', action='store_true', help='Estimate the best final tree based on all loci in partitioned analysis')
    parser.add_argument('--estimate_best_concat_model', action='store_true', help='Estimate the best model based on all loci in concatenated analysis')
    parser.add_argument('--test_final_tree', action='store_true', help='Test the final best tree, compare with the tree inferred without the inferred model')
    parser.add_argument('--cross_validation', action='store_true', help='Test the performance of final model and tree on all loci with comparison with initial model and tree estimated without inferred model.')
    parser.add_argument('--final_tree_tool', type=str, default='IQFAST', choices=['IQ',"IQFAST",'FT'], help='Method to estimate the final tree (IQ-TREE[IQ] / IQ-TREE in -fast option [IQFAST] / FastTree[FT]) (default: IQ)')
    parser.add_argument('--fix_subtree_num', action='store_true', help='Fix the number of subtrees during model estimation')
    parser.add_argument('--fix_subtree_topology', action='store_true', help='Fix the topology of subtrees during model estimation')

    parser.add_argument('--use_outgroup', action='store_true', help='Use outgroup in the tree estimation')
    parser.add_argument('--outgroup_taxa_list', type=Path, help='Path to the list of outgroup taxa to select from.')

    parser.add_argument('--tree_size_lower_lim', type=int, default=15, help='Lower limit for the size of subtrees (default: 15)')
    parser.add_argument('--tree_size_upper_lim', type=int, default=100, help='Upper limit for the size of subtrees (default: 100)')  
    parser.add_argument('--prune_mode', type=str, default='split', choices=['split', 'lower', 'upper', 'deep'], help="Pruning mode (split/lower/upper/deep) (default: split)")

    parser.add_argument('--integrity_filter', type=float, default=0, help='Threshold of integrity for every site')
    parser.add_argument('--nstatus_filter', type=int, default=20, help='Threshold of character status number for every site')

    parser.add_argument('-S', '--model_update_summary', action='store_true', help='Enable model update summary inner each iteration')
    parser.add_argument('-R', '--tree_comparison_report', action='store_true', help='Enable tree comparison report when comparing pair of trees')
    parser.add_argument('-c', '--keep_cmd_output', action='store_true', help='Keep detailed command output in the log file')
    parser.add_argument('-t', '--keep_tmp', action='store_true', help='Keep temporary files')
    parser.add_argument('-A', '--keep_aln', action='store_true', help='Keep training and testing alignment files.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print commands in logfile')

    parser.add_argument('--output_dir', type=Path, required=True, help='Output directory')
    parser.add_argument('--FastTreeMP_path', type=Path, required=True, help='Path to the FastTreeMP executable')
    return parser.parse_args() 

if __name__ == "__main__":
    args = cli()
    args.output_dir = args.output_dir / f"{args.prefix}"  
    args.output_dir.mkdir(parents=True, exist_ok=True)
    metalogger = MetaLogger.get_instance(str(args.output_dir / "meta.json"))
    metalogger.log_parameters({k: str(v) if isinstance(v, PosixPath) else v for k, v in vars(args).items()})
    metalogger.log_parameter("keep_model_thres", keep_model_thres)
    metalogger.log_parameter("code_version", "2024-07-31")
    metalogger.log_parameter("start_time", time.strftime("%Y-%m-%d %H:%M:%S"))
    start_time = time.time()
    args.taxa_list = Path(args.taxa_list)
    main(args)
    end_time = time.time()
    total_time = end_time - start_time
    log_message('result', f"Total time usage: {total_time:.2f} seconds ({total_time/3600:.2f} h)")
    metalogger.log_parameter("end_time", time.strftime("%Y-%m-%d %H:%M:%S"))
    metalogger.log_parameter("total_time", total_time)