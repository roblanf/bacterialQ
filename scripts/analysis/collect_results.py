#!/usr/bin/env python3
import os
import shutil
import re
from glob import glob
import subprocess
import numpy as np
import csv
import argparse
import sys

file_path = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(file_path)))
from Q_convert import extract_Q_from_nex, AminoAcidSubstitutionModel
from models_dist_table import *

def combine_csv_sum(input_file, output_file):
    """
    Combine summary files formatted in csv.
    """
    if not os.path.exists(output_file) or os.stat(output_file).st_size == 0:
        shutil.copy(input_file, output_file)
    else:
        with open(input_file, 'r') as f:
            next(f)  # skip header line
            with open(output_file, 'a') as out:
                shutil.copyfileobj(f, out)

def extract_last_treefile(directory, destination):
    """
    Extract specific tree files from the estimated_tree directory and rename them.
    
    Args:
        directory (str): Path to the directory containing loop directories.
        destination (str): Path to the destination directory.
    """
    estimated_tree_dir = os.path.join(directory, 'estimated_tree')
    treefile = os.path.join(estimated_tree_dir, 'FinalModel_FT_All_G20.treefile')
    if os.path.exists(treefile):
        new_treefile_name = os.path.basename(directory) + '_FinalModel_FT.treefile'
        shutil.copy(treefile, os.path.join(destination, new_treefile_name))

def extract_phylum_name(string):
    """
    Extract the phylum name from a string using regex.

    Returns:
        str: Extracted phylum name or 'Unknown' if not found.
    """
    # match = re.search(r'p__(.*?)_\d{2,}', string)
    match = re.search(r'Q\.(.*)', string)
    if match:
        phylum_name = match.group(1)
    else:
        phylum_name = 'Unknown'
    return phylum_name

def process_directory(result_dir, sum_dir='./'):
    """
    Process a directory to extract and combine results.
    """
    if os.path.exists(os.path.join(result_dir, 'final_test', 'tree_comparison.html')):
        extract_last_treefile(result_dir, os.path.join(sum_dir, 'treefiles'))
        combine_csv_sum(os.path.join(result_dir, 'iqtree_results.csv'), os.path.join(sum_dir, 'combined_iqtree_sum.csv'))
        combine_csv_sum(os.path.join(result_dir, 'tree_summary.csv'), os.path.join(sum_dir, 'combined_tree_sum.csv'))
        Q_matrix = extract_Q_from_nex(os.path.join(result_dir, 'inferred_models', 'trained_model.nex'))
        for i in range(len(Q_matrix)):
            Q_matrix[i].add_Q_to_nex(os.path.join(sum_dir, 'trained_models_all.nex'))
        last_model = Q_matrix[-1]
        last_model.model_name = re.sub(r'_\d+$', '', last_model.model_name)
        last_model.add_Q_to_nex(os.path.join(sum_dir, 'trained_models_last.nex'))
        shutil.copy(os.path.join(result_dir, 'log.md'), os.path.join(sum_dir, 'logfiles', '{}_log.md'.format(os.path.basename(result_dir))))
        phylum_name = extract_phylum_name(result_dir)
        with open(os.path.join(sum_dir, 'phylum_list.txt'), 'a') as f:
            f.write(phylum_name + '\n')

def filter_directories(root_directory, regex):
    """
    Filter directories in the root directory based on a regex pattern.
    
    Args:
        root_directory (str): Path to the root directory.
        regex (str): Regex pattern to filter directories.
    
    Returns:
        list: List of filtered directories.
    """
    filtered_directories = []
    for directory in os.listdir(root_directory):
        full_directory = os.path.join(root_directory, directory)
        if os.path.isdir(full_directory) and re.match(regex, directory):
            filtered_directories.append(full_directory)
    return filtered_directories

def integrate_phylogenetic_models(directory_list, sum_dir='./summary'):
    """
    Integrate phylogenetic models from a list of directories.
    
    Args:
        directory_list (list): List of directories.
        sum_dir (str): Path to the summary directory.
    """
    treefiles_dir = os.path.join(sum_dir, 'treefiles')
    if not os.path.exists(treefiles_dir):
        os.makedirs(treefiles_dir)
    logfiles_dir = os.path.join(sum_dir, 'logfiles')
    if not os.path.exists(logfiles_dir):
        os.makedirs(logfiles_dir)
    
    for directory in directory_list:
        process_directory(directory, sum_dir)

def plot_model(existed_model_nex, trained_model_nex, sum_res):
    """
    Plot models using PCA and t-SNE.
    
    Args:
        existed_model_nex (str): Path to the existed model .nex file.
        trained_model_nex (str): Path to the trained model .nex file.
        sum_res (str): Path to the summary results directory.
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)

    pca_script = os.path.join(parent_dir, "PCA_Q.R")
    tsne_script = os.path.join(parent_dir, "tSNE_Q.R")

    subprocess.run(["Rscript", pca_script, existed_model_nex, trained_model_nex, sum_res])
    subprocess.run(["Rscript", tsne_script, existed_model_nex, trained_model_nex, sum_res])
    subprocess.run(["Rscript", pca_script, "NULL", trained_model_nex, sum_res])
    subprocess.run(["Rscript", tsne_script, "NULL", trained_model_nex, sum_res])

def main(root_directory, sum_dir, regex, existed_model_nex):
    """
    Main function to process directories and plot models.
    
    Args:
        root_directory (str): Path to the root directory.
        sum_dir (str): Path to the summary directory.
        regex (str): Regex pattern to filter directories.
        existed_model_nex (str): Path to the existed model .nex file.
    """
    trained_model_nex = os.path.join(sum_dir, 'trained_models_last.nex')
    if not os.path.exists(sum_dir):
        os.makedirs(sum_dir)

    # Process directories and integrate phylogenetic models
    filtered_directories = filter_directories(root_directory, regex)
    integrate_phylogenetic_models(filtered_directories, sum_dir)
    # Visualise models using PCA and t-SNE (R code)
    plot_model(existed_model_nex, trained_model_nex, sum_dir)

    # Calculate corrlation and distance between trained and existed models
    correlations, distances, model_names = calculate_trained_models_dist(trained_model_nex)
    save_to_csv(correlations, distances, model_names, model_names, os.path.join(sum_dir, 'trained_models_dist.csv'))
    # Calculate corrlation and distance among trained models
    correlations, distances, model_names1, model_names2 = calculate_all_models_dist(trained_model_nex, existed_model_nex)
    save_to_csv(correlations, distances, model_names1, model_names2, os.path.join(sum_dir, 'all_models_dist.csv'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some directories and models.')
    parser.add_argument('-i', '--input', help='Input root directory', required=True)
    parser.add_argument('-o', '--output', help='Output directory', default='./summary')
    parser.add_argument('-r', '--regex', help='Regex pattern', default='.*')
    parser.add_argument('-n', '--nex', help='Path to existed model.nex', required=True)

    args = parser.parse_args()

    main(args.input, args.output, args.regex, args.nex)