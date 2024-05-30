# This version is a semi-finished-product for integrate subtrees method in. Need to be called by run_phylum_iteration_0416.sh

#!/usr/bin/env python3
import argparse
import subprocess
import time
import os
import sys
import shutil
import logging
from pathlib import Path
from typing import Tuple

# Import functional scrpits
# Packages need: numpy Bio
# Packages need for plot: pandas matplotlib seaborn (Q_convert.bubble_plot, grep_iqtree_output.plot_loci_statistic)
from Q_convert import *
from grep_iqtree_output import *
from make_subtree import *
from concat_seq import *

def log_and_handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"Running {func.__name__}...")
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Log the error and re-raise the exception
            logging.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

def run_command(cmd: str, log_file: str, log_any: bool = True,log_output: bool = False, log_time: bool = False) -> Tuple[str, str, int]:
    """
    Run a shell command, log its output, and return its output and exit code.

    Args:
        cmd (str): The command to run.
        log_file (str): The path to the log file.
        log_output (bool, optional): Whether to log the stdout of the command. Defaults to False.
        log_time (bool, optional): Whether to log the runtime of the command. Defaults to True.

    Returns:
        Tuple[str, str, int]: A tuple containing the standard output, standard error, and exit code of the command.
    """
    if args.verbose:
        print(cmd, "\n")
    
    start_time = time.time()
    process = subprocess.Popen(cmd, shell=True, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_code = process.returncode
    end_time = time.time()
    run_time = end_time - start_time

    with open(log_file, 'a') as f:
        if log_any:
            f.write(f"  Command: {cmd}\n")
            if stderr:
                f.write(f"  Error:\n{stderr}")
            if log_output and stdout:
                f.write(f"  Output:\n{stdout}")
            f.write(f"  Exit code: {exit_code}\n")
            if log_time:
                f.write(f"  Runtime: {run_time:.2f} seconds\n")

    if exit_code > 0:
        sys.exit(stderr)

    return stdout, stderr, exit_code

def check_params(args: argparse.Namespace) -> None:
    """
    Check if required command line arguments are provided and valid.

    Args:
        args (argparse.Namespace): Command line arguments.
    """
    if not args.prefix or not args.tree_file or not args.train_loc_path or not args.test_loc_path or not args.model_dir:
        sys.exit("Missing required parameters: -prefix, -tree_file, -train_loc_path, -test_loc_path, -model_dir")

@log_and_handle_error
def get_subtrees(args):
    tree = Phylo.read(args.tree_file, "newick")
    taxa_dic = read_taxa_list(args.taxa_list)
    
    IS_MULTI_TREE = True if os.path.isdir(args.taxa_list) else False
    
    subtree_dic = trim_subtrees(tree, taxa_dic)
    write_subtrees(subtree_dic, f"{args.output_dir}/subtrees")
    
    return IS_MULTI_TREE

def check_empty_seq(file_path):
    """
    Check if a fasta file contains only empty sequences (? or -).

    Args:
        file_path (str): Path to the fasta file.

    Returns:
        bool: True if the file contains only empty sequences, False otherwise.
    """
    for record in SeqIO.parse(file_path, "fasta"):
        seq = str(record.seq).replace("?", "").replace("-", "")
        if seq:
            return False
    return True

@log_and_handle_error
def split_loci(args: argparse.Namespace) -> None:
    """
    Split alignments into training and testing sets based on predefined folders and filtered loci list.

    Args:
        args (argparse.Namespace): Command line arguments.
    """
    logging.info("Splitting alignments into testing and training")
    
    train_loci_dir = Path(args.output_dir) / "loci" / "training_loci"
    test_loci_dir = Path(args.output_dir) / "loci" / "testing_loci"
    train_loci_dir.mkdir(parents=True, exist_ok=True)
    test_loci_dir.mkdir(parents=True, exist_ok=True)

    if args.loci_list and os.path.getsize(args.loci_list) > 0:
        with open(args.loci_list, 'r') as f:
            filtered_loci = f.read().splitlines()
            train_loci_files = [f for f in Path(args.train_loc_path).glob("*.fa*") if f.name in filtered_loci]
            test_loci_files = [f for f in Path(args.test_loc_path).glob("*.fa*") if f.name in filtered_loci]
    else:
        train_loci_files = [f for f in Path(args.train_loc_path).glob("*.fa*")]
        test_loci_files = [f for f in Path(args.test_loc_path).glob("*.fa*")]
    
    if not train_loci_files or not test_loci_files:
        raise ValueError("Training or testing loci set is empty after filtering. Program will terminate.")
    
    logging.info(f"Number of training loci: {len(train_loci_files)}")
    logging.info(f"Number of testing loci: {len(test_loci_files)}")

    def check_empty_seq(file_path):
        with open(file_path, 'r') as f:
            content = f.read().splitlines()
            for line in content:
                if line.startswith('>'):
                    continue
                if line.strip('-?'):
                    return False
        return True

    def run_faSomeRecords(loci_files, taxa_list, output_dir):
        if os.path.isfile(taxa_list):
            for file in loci_files:
                file_name = os.path.basename(file)
                output_file = output_dir / file_name
                cmd = f"faSomeRecords {file} {taxa_list} {output_file}"
                run_command(cmd, f"{args.output_dir}/log.txt", log_any=False)
                if check_empty_seq(output_file):
                    os.remove(output_file)
                    logging.info(f"Removed empty sequence file: {output_file}")
        elif os.path.isdir(taxa_list):
            for tree_file in os.listdir(taxa_list):
                if tree_file.endswith(".txt"):
                    tree_name = os.path.splitext(tree_file)[0]
                    for file in loci_files:
                        loci_name = os.path.splitext(os.path.basename(file))[0]
                        ext = os.path.splitext(file)[1]
                        output_file = Path(f"{output_dir}/{tree_name}_{loci_name}{ext}")
                        cmd = f"faSomeRecords {file} {os.path.join(taxa_list, tree_file)} {output_file}"
                        run_command(cmd, f"{args.output_dir}/log.txt", log_any=False)
                        if check_empty_seq(output_file):
                            os.remove(output_file)
                            logging.info(f"Removed empty sequence file: {output_file}")
        else:
            raise ValueError(f"{taxa_list} is neither a file nor a directory.")

    run_faSomeRecords(train_loci_files, args.taxa_list, train_loci_dir)
    run_faSomeRecords(test_loci_files, args.taxa_list, test_loci_dir)
    
    logging.info("Finished splitting alignments")

@log_and_handle_error
def initial_model_estimation(args: argparse.Namespace) -> Tuple[AminoAcidSubstitutionModel, str]:
    """
    Estimate initial amino acid substitution models using IQ-TREE2.

    Args:
        args (argparse.Namespace): Command line arguments.

    Returns:
        Tuple[AminoAcidSubstitutionModel, str]: The best initial model and its name.
    """
    estimate_dir = Path(args.output_dir) / "estimate" / "initial"
    estimate_dir.mkdir(parents=True, exist_ok=True)
    
    train_loci_dir = Path(args.output_dir) / "loci" / "training_loci"
    num_train_loci = len(list(train_loci_dir.glob('*')))
    num_thread_used = min(num_train_loci, args.max_threads)

    cmd = f"iqtree -T {num_thread_used} -p {train_loci_dir} -m MFP -cmax 8 -mset LG,Q.PFAM,Q.INSECT,Q.YEAST,MTMET,MTART -te {args.output_dir}/{args.prefix}_reference.tree -pre {estimate_dir}/{args.prefix}.initial"
    # -T: number of threads
    # -p: path to the directory containing training loci alignments
    # -m: model selection option (MF: ModelFinder)
    # -cmax: maximum number of categories for FreeRate model (8)
    # -te: reference tree file
    # -pre: prefix for output files

    run_command(cmd, f"{args.output_dir}/log.txt", log_output=args.keep_cmd_output, log_time=True)

    initial_best_model_name = run_command(f"./analyze_best_models.sh {estimate_dir}/{args.prefix}.initial.best_scheme.nex {estimate_dir}/models.txt", f"{args.output_dir}/log.txt")[0]

    logging.info(f"The best model for the initial estimation is {initial_best_model_name}")

    initial_best_model = extract_spc_Q_from_nex(args.model_dir, initial_best_model_name)
    initial_best_model.rescale_Q_matrix()

    # Plot scatterplot of site number to proportion of informative site
    plot_loci_statistic(f"{estimate_dir}/{args.prefix}.initial.iqtree", f"{args.output_dir}/loci_statistic.png")
    # Write statistic of iqtree to csv file
    write_iqtree_statistic(f"{estimate_dir}/{args.prefix}.initial.iqtree", f"{args.prefix}_initial_{initial_best_model_name}",f"{args.output_dir}/iqtree_results.csv")
    
    return initial_best_model, initial_best_model_name

@log_and_handle_error
def verify_models(args: argparse.Namespace, using_models: str, verify_dir: Path, nex_model_set: str = None) -> str:
    """
    Verify models on test loci using IQ-TREE2.

    Args:
        args (argparse.Namespace): Command line arguments.
        using_models (str): Comma-separated list of models to use.
        verify_dir (Path): Directory for model verification output.
        nex_model_set (str, optional): Path to a nexus file containing the models to use. Defaults to None.

    Returns:
        str: The name of the best model based on model verification.
    """
    verify_dir.mkdir(exist_ok=True)

    test_loci_dir = Path(args.output_dir) / "loci" / "testing_loci"
    num_test_loci = len(list(test_loci_dir.glob('*')))
    num_thread_used = min(num_test_loci, args.max_threads)
    if not nex_model_set:
        # If no nexus file is provided, use the comma-separated list of models
        cmd = f"iqtree -T {num_thread_used} -S {test_loci_dir} -m MF -mset {using_models} -pre {verify_dir}/test_{args.prefix}"
    else:
        # If a nexus file is provided, use the models defined in the file
        cmd = f"iqtree -T {num_thread_used} -S {test_loci_dir} -m MF -mset {using_models} -mdef {nex_model_set} -pre {verify_dir}/test_{args.prefix}"
    run_command(cmd, f"{args.output_dir}/log.txt", log_output=args.keep_cmd_output, log_time=True)

    # Read the best model name from the IQ-TREE output nexus file
    best_model_name = run_command(f"./analyze_best_models.sh {verify_dir}/test_{args.prefix}.best_scheme.nex {verify_dir}/models.txt", f"{args.output_dir}/log.txt")[0].strip()  
    return best_model_name

@log_and_handle_error
def two_step_iteration(args: argparse.Namespace, initial_best_model: AminoAcidSubstitutionModel, initial_best_model_name: str) -> str:
    """
    The core function to perform full-constrainted iterative model estimation and tree re-estimation.

    Args:
        args (argparse.Namespace): Command line arguments. 
        initial_best_model (AminoAcidSubstitutionModel): The best initial model.
        initial_best_model_name (str): The name of the best initial model.

    Returns:
        str: The name of the best model after iterations.
    """
    prev_model = initial_best_model
    prev_tree = f"{args.output_dir}/estimate/initial/{args.prefix}.initial.treefile"
    model_list = list_Q_from_nex(args.model_dir)
    i = 1

    trained_model_nex = f"{args.output_dir}/trained_models.nex"
    train_loci_dir = Path(args.output_dir) / "loci" / "training_loci"
    num_train_loci = len(list(train_loci_dir.glob('*')))
    num_thread_used = min(num_train_loci, args.max_threads)
    concat_loci = "/mnt/data/dayhoff/home/u7457359/project/GTDB/GTDB_TREE/data/train_concat_seq.faa"

    while True:
        loop_dir = Path(args.output_dir) / f"estimate/loop_{i}"
        model_update_dir = loop_dir / "model_update"
        tree_update_dir = loop_dir / "tree_update"
        model_update_dir.mkdir(parents=True, exist_ok=True)
        tree_update_dir.mkdir(parents=True, exist_ok=True)

        logging.info(f"Iteration {i}: Estimating Q matrix with IQ-TREE2")
        
        # With -te and -p, IQ-TREE would estimate model under fixed tree topology, with all trees share the same topology but free on overall evolutionary speed
        if args.mode == "fullcon":
            if prev_model.model_name.upper() in model_list:
                # If the previous model is in the initial model list, use its name directly
                cmd = f"iqtree -T {num_thread_used} -p {train_loci_dir} -te {prev_tree} --init-model {prev_model.model_name} --model-joint GTR20+FO -pre {model_update_dir}/{args.prefix}_{i}"
            else:
                # If the previous model is a newly trained model, use the model file in the output directory
                cmd = f"iqtree -T {num_thread_used} -p {train_loci_dir} -te {prev_tree} --init-model {args.output_dir}/trained_models/{prev_model.model_name} --model-joint GTR20+FO -pre {model_update_dir}/{args.prefix}_{i}"
        # With -te and -Q,  IQ-TREE would estimate model under fixed tree topology, with all trees share the same topology but free on each branch length
        elif args.mode == "topocon":
            if prev_model.model_name.upper() in model_list: 
                # If the previous model is in the initial model list, use its name directly
                cmd = f"iqtree -T {num_thread_used} -Q {train_loci_dir} -te {prev_tree} --init-model {prev_model.model_name} --model-joint GTR20+FO -pre {model_update_dir}/{args.prefix}_{i}"
            else:
                # If the previous model is a newly trained model, use the model file in the output directory
                cmd = f"iqtree -T {num_thread_used} -Q {train_loci_dir} -te {prev_tree} --init-model {args.output_dir}/trained_models/{prev_model.model_name} --model-joint GTR20+FO -pre {model_update_dir}/{args.prefix}_{i}"

        run_command(cmd, f"{args.output_dir}/log.txt", log_output=args.keep_cmd_output, log_time=True)

        logging.info(f"Iteration {i}: Extracting Q matrix")
        
        iqtree_file = f"{model_update_dir}/{args.prefix}_{i}.iqtree"
        prev_tree = f"{loop_dir}/model_update/{args.prefix}_{i}.treefile"

        # Extract the Q matrix from the IQ-TREE output file
        new_model = extract_Q_from_iqtree(f"{args.prefix}_{i}", iqtree_file)
        # Convert the Q matrix to the format required by FastTree
        new_model.convert_to_fasttree(model_update_dir)
        # Add the Q matrix to the nexus file containing trained models
        new_model.add_Q_to_nex(trained_model_nex)

        # Write statistic of iqtree to csv file   
        write_iqtree_statistic(iqtree_file, f"{args.prefix}loop{i}",f"{args.output_dir}/iqtree_results.csv")
        # Save the model parameters to a file in the output directory
        with open(f"{args.output_dir}/trained_models/{new_model.model_name}", 'w') as f:
            f.write(new_model.print_parameter())

        logging.info(f"Iteration {i}: Re-estimating the tree with VeryFastTree")
        # Now just using FastTree in single core instead of VeryFastTree
        # cmd_FT = f"fasttree -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -mlacc 2 {concat_loci} > {tree_update_dir}/{args.prefix}_{i}.treefile"
        # Retry veryfasttree on larger dataste..
        if num_thread_used >= 20:
            cmd_FT = f"VeryFastTree -threads {num_thread_used} -threads-level 1 -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -mlacc 2 {concat_loci} > {tree_update_dir}/{args.prefix}_{i}.treefile"
        else:
            cmd_FT = f"VeryFastTree -threads-level 1 -trans {model_update_dir}/Q_matrix_fasttree.txt -gamma -spr 4 -mlacc 2 {concat_loci} > {tree_update_dir}/{args.prefix}_{i}.treefile"
        
        run_command(cmd_FT, f"{args.output_dir}/log.txt", log_output=args.keep_cmd_output, log_time=True)
        new_tree = f"{loop_dir}/tree_update/{args.prefix}_{i}.treefile"

        # Compare the new tree with the previous tree using R
        cmd_R = f"""
        Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '{loop_dir}', params = list(tree1_path = '{prev_tree}', tree2_path = '{new_tree}'))"
        """
        run_command(cmd_R, f"{args.output_dir}/log.txt")

        # Compare the current model with the previous model using bubble plot
        bubble_plot(new_model, f"{loop_dir}/{args.prefix}_model_{i}.png")
        bubble_difference_plot(prev_model, new_model, f"{loop_dir}/{args.prefix}_model_diff_{i}.png")
        
        if args.verify_on_loop:
            # If model verification is enabled, verify the models on test loci
            model_to_test = initial_best_model_name + "," + ",".join(list_Q_from_nex(trained_model_nex))
            verify_dir = loop_dir / "model_verification"
            logging.info(f"Iteration {i}: Model verification results")
            best_model_name = verify_models(args, model_to_test, verify_dir, trained_model_nex)
            logging.info(f"Best model for iteration {i}: {best_model_name}")
            if best_model_name != new_model.model_name:
                logging.warning(f"Model {best_model_name} is better than the current model {new_model.model_name}")

        logging.info(f"Iteration {i}: Checking convergence")
        ifconverge, corr, dist = prev_model.check_convergence(new_model, threshold=args.converge_thres)
        logging.info(f"Pearson's correlation: {corr}")
        logging.info(f"Euclidean distance: {dist}")
        if ifconverge:
            # If convergence is reached, stop the iteration
            logging.info(f"Convergence reached at iteration {i}")
            break
        
        i += 1
        prev_model = new_model
        prev_tree = new_tree
        if i > args.max_iterate:
            # If the maximum number of iterations is reached, stop the iteration
            logging.info(f"Stop loop after {args.max_iterate} times of iteration")
            break
        
        if not args.keep_tmp:
            # If temporary files are not kept, remove the concatenated alignment file
            os.remove(concat_loci)

    # Plot PCA of Q matrices and state frequencies among initial and trained models
    cmd = f"Rscript PCA_Q.R {args.model_dir} {args.output_dir}/trained_models.nex {args.output_dir}/trained_models"
    run_command(cmd, f"{args.output_dir}/log.txt")

    if args.verify_on_loop:
        # If model verification is enabled, return the best model name from the last iteration
        return best_model_name
    else:
        # If model verification is not enabled, verify the models on test loci after all iterations
        model_to_test = initial_best_model_name + "," + ",".join(list_Q_from_nex(trained_model_nex))
        verify_dir = Path(args.output_dir) / "final_verification"
        logging.info("Final model verification results")
        best_model_name = verify_models(args, model_to_test, verify_dir, trained_model_nex)
        return best_model_name
    
@log_and_handle_error
def one_step_iteration(args: argparse.Namespace, initial_best_model: AminoAcidSubstitutionModel, initial_best_model_name: str) -> str:
    """
    The core function to perform iterative model estimation and tree re-estimation under semi-constaint and non-constainted scenarios.
    Args:
        args (argparse.Namespace): Command line arguments.
        initial_best_model (AminoAcidSubstitutionModel): The best initial model.
        initial_best_model_name (str): The name of the best initial model.

    Returns:
        str: The name of the best model after iterations.
    """
    prev_model = initial_best_model
    prev_tree = f"{args.output_dir}/estimate/initial/{args.prefix}.initial.treefile"
    model_list = list_Q_from_nex(args.model_dir)
    i = 1

    trained_model_nex = f"{args.output_dir}/trained_models.nex"
    train_loci_dir = Path(args.output_dir) / "loci" / "training_loci"
    num_train_loci = len(list(train_loci_dir.glob('*')))
    num_thread_used = min(num_train_loci, args.max_threads)

    while True:
        loop_dir = Path(args.output_dir) / f"estimate/loop_{i}"
        loop_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Iteration {i}: Estimating Q matrix with IQ-TREE2")
        
        # With out -te, IQ-TREE would estimate a new tree on ML method, with all trees share the same topology but free on overall evolutionary speed
        if args.mode == "topolink":
            if prev_model.model_name.upper() in model_list:
                # If the previous model is in the initial model list, use its name directly
                cmd = f"iqtree -T {num_thread_used} -p {train_loci_dir} --init-model {prev_model.model_name} --model-joint GTR20+FO -pre {loop_dir}/{args.prefix}_{i}"
            else:
                # If the previous model is a newly trained model, use the model file in the output directory
                cmd = f"iqtree -T {num_thread_used} -p {train_loci_dir} --init-model {args.output_dir}/trained_models/{prev_model.model_name} --model-joint GTR20+FO -pre {loop_dir}/{args.prefix}_{i}"
        elif args.mode == "noncon":
        # With-S, IQ-TREE would re-estimate the tree for every single locus, with all trees have individual topology and branch length
            if prev_model.model_name.upper() in model_list:
                # If the previous model is in the initial model list, use its name directly
                cmd = f"iqtree -T {num_thread_used} -S {train_loci_dir} --init-model {prev_model.model_name} --model-joint GTR20+FO -pre {loop_dir}/{args.prefix}_{i}"
            else:
                # If the previous model is a newly trained model, use the model file in the output directory
                cmd = f"iqtree -T {num_thread_used} -S {train_loci_dir} --init-model {args.output_dir}/trained_models/{prev_model.model_name} --model-joint GTR20+FO -pre {loop_dir}/{args.prefix}_{i}"

        run_command(cmd, f"{args.output_dir}/log.txt", log_output=args.keep_cmd_output, log_time=True)

        logging.info(f"Iteration {i}: Extracting Q matrix")
        
        iqtree_file = f"{loop_dir}/{args.prefix}_{i}.iqtree"
        # Extract the Q matrix from the IQ-TREE output file
        new_model = extract_Q_from_iqtree(f"{args.prefix}_{i}", iqtree_file)
        # Convert the Q matrix to the format required by FastTree
        new_model.add_Q_to_nex(trained_model_nex)
        # Todo: Normalise the multi tree length to compate it with origin model / use Astral
        # Write statistic of iqtree to csv file
        write_iqtree_statistic(iqtree_file, f"{args.prefix}_loop_{i}",f"{args.output_dir}/iqtree_results.csv")

        # Save the model parameters to a file in the output directory
        with open(f"{args.output_dir}/trained_models/{new_model.model_name}", 'w') as f:
            f.write(new_model.print_parameter())

        new_tree = f"{loop_dir}/{args.prefix}_{i}.treefile"
        # Todo: Develop multi-tree comparison with summays of topology changes (maybe further apply for subtree method...)
        # Compare the new tree with the previous tree using R
        # cmd_R = f"""
        # Rscript -e "rmarkdown::render('tree_comparison.Rmd', output_dir= '{loop_dir}', params = list(tree1_path = '{prev_tree}', tree2_path = '{new_tree}'))"
        # """
        # run_command(cmd_R, f"{args.output_dir}/log.txt")

        # Compare the current model with the previous model using bubble plot
        bubble_plot(new_model, f"{loop_dir}/{args.prefix}_model_{i}.png")
        bubble_difference_plot(prev_model, new_model, f"{loop_dir}/{args.prefix}_model_diff_{i}.png")
        
        if args.verify_on_loop:
            # If model verification is enabled, verify the models on test loci
            model_to_test = initial_best_model_name + "," + ",".join(list_Q_from_nex(trained_model_nex))
            verify_dir = loop_dir / "model_verification"
            logging.info(f"Iteration {i}: Model verification results")
            best_model_name = verify_models(args, model_to_test, verify_dir, trained_model_nex)
            logging.info(f"Best model for iteration {i}: {best_model_name}")
            if best_model_name != new_model.model_name:
                logging.warning(f"Model {best_model_name} is better than the current model {new_model.model_name}")

        logging.info(f"Iteration {i}: Checking convergence")
        if prev_model.check_convergence(new_model, threshold=args.converge_thres):
            # If convergence is reached, stop the iteration
            logging.info(f"Convergence reached at iteration {i}")
            break
        
        i += 1
        prev_model = new_model
        prev_tree = new_tree
        if i > args.max_iterate:
            # If the maximum number of iterations is reached, stop the iteration
            logging.info(f"Stop loop after {args.max_iterate} times of iteration")
            break

    # Plot PCA of Q matrices and state frequencies among initial and trained models
    cmd = f"Rscript PCA_Q.R {args.model_dir} {args.output_dir}/trained_models.nex {args.output_dir}/trained_models"
    run_command(cmd, f"{args.output_dir}/log.txt")

    if args.verify_on_loop:
        # If model verification is enabled, return the best model name from the last iteration
        return best_model_name
    else:
        # If model verification is not enabled, verify the models on test loci after all iterations
        model_to_test = initial_best_model_name + "," + ",".join(list_Q_from_nex(trained_model_nex))
        verify_dir = Path(args.output_dir) / "final_verification"
        logging.info("Final model verification results")
        best_model_name = verify_models(args, model_to_test, verify_dir, trained_model_nex)
        return best_model_name
    
def main(args: argparse.Namespace) -> None:
    """
    Main function to run the model estimation pipeline.
    """
    check_params(args)
    
    logging.basicConfig(filename=f"{args.output_dir}/log.txt", level=logging.INFO, format='%(message)s')
    logging.info(f"Running model estimation with the following parameters:")
    logging.info(f"  Constraint mode: {args.mode}")
    logging.info(f"  Maximum iterations: {args.max_iterate}")
    logging.info(f"  Convergence threshold: {args.converge_thres}")
    logging.info(f"  File prefix: {args.prefix}")
        
    IS_MULTI_TREE = get_subtrees(args)
    logging.info(f"Multi-tree mode: {IS_MULTI_TREE}")
    
    get_a_subtree(args.tree_file, args.taxa_list, f"{args.output_dir}/{args.prefix}_reference.tree")
    split_loci(args)
    
    initial_best_model, initial_best_model_name = initial_model_estimation(args)
    
    if args.mode in ["topolink", "noncon"]:
        best_model_name = one_step_iteration(args, initial_best_model, initial_best_model_name)
    elif args.mode in ["fullcon", "topocon"]:
        best_model_name = two_step_iteration(args, initial_best_model, initial_best_model_name)
    else:
        raise ValueError("Only four kinds of modes are supported: fullcon, topocon, topolink and noncon")

    if best_model_name != initial_best_model_name:
        best_model = extract_spc_Q_from_nex(f"{args.output_dir}/trained_models.nex", best_model_name)
        best_model.add_Q_to_nex(Path(args.summary_dir) / "best_trained_models.nex")
    else:
        logging.info("No better model found. The initial model is the best.")

    if not args.keep_tmp:
        shutil.rmtree(f"{args.output_dir}/loci", ignore_errors=True)

def cli() -> argparse.Namespace:
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser()
    # File path
    parser.add_argument('--train_loc_path', type=str, help='Path to the directory containing training loci alignments')
    parser.add_argument('--test_loc_path', type=str, help='Path to the directory containing testing loci alignments')
    parser.add_argument('--loci_list', type=str, help='File containing the list of filtered loci')
    parser.add_argument('--tree_file', type=str, help='Tree file')
    parser.add_argument('--taxa_list', type=str, help='File of taxa list used for training')
    parser.add_argument('--model_dir', type=str, help='Directory of nexus files containing initial models')
    # Iteration settings
    parser.add_argument('-T', '--max_threads', type=int, default=100, help='Maximum number of threads')
    parser.add_argument('-l', '--max_iterate', type=int, default=5, help='Maximum number of iterations')
    parser.add_argument('-m', '--mode',  type=str, default="fullcon", help='Mode of constraint in model estimating (fullcon/topocon/topolink/noncon)')
    parser.add_argument('--converge_thres', type=float, default=0.999, help='Convergence threshold of Q matrix')
    parser.add_argument('--verify_on_loop', action='store_true', help='Verify models on test loci during iteration')
    # Output and logging settings
    parser.add_argument('--keep_tmp', action='store_true', help='Keep temporary files')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print commands')
    parser.add_argument('-p', '--prefix', type=str, default="Q", help='Prefix for output files')
    parser.add_argument('-c', '--keep_cmd_output', action='store_true', help='Keep detailed command output in the log file')
    # Path to format all analysis and summary them up
    parser.add_argument('--output_dir', type=str, help='Directory for output repository')
    parser.add_argument('--summary_dir', type=str, help='Directory for summary across all models')
    return parser.parse_args()

if __name__ == "__main__":
    args = cli()
    main(args)