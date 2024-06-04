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

def combine_iqtree_sum(input_file, output_file):
    if not os.path.exists(output_file) or os.stat(output_file).st_size == 0:
        shutil.copy(input_file, output_file)
    else:
        with open(input_file, 'r') as f:
            next(f)  # skip header line
            with open(output_file, 'a') as out:
                shutil.copyfileobj(f, out)

def extract_last_treefile(directory, destination):
    # Get all the loop directories in the given directory
    loop_dirs = sorted(glob(os.path.join(directory, 'loop_*')))
    
    # Get the last loop directory
    last_loop_dir = loop_dirs[-1]
    
    # Get the .treefile in the tree_update directory of the last loop
    treefile = glob(os.path.join(last_loop_dir, 'tree_update', '*.treefile'))[0]
    
    # Copy the treefile to the destination directory
    shutil.copy(treefile, destination)

def extract_phylum_name(string):
    # Extract the phylum name using regex
    match = re.search(r'p__(.*?)_\d{2,}', string)
    if match:
        phylum_name = match.group(1)
    else:
        phylum_name = 'Unknown'
    return phylum_name

def process_directory(result_dir, sum_dir='./'):
    if os.path.exists(os.path.join(result_dir, 'final_test', 'tree_comparison.html')):
        extract_last_treefile(result_dir, os.path.join(sum_dir, 'treefiles'))
        combine_iqtree_sum(os.path.join(result_dir, 'iqtree_results.csv'), os.path.join(sum_dir, 'combined_iqtree_sum.csv'))
        Q_matrix = extract_Q_from_nex(os.path.join(result_dir, 'trained_models', 'trained_model.nex'))
        for i in range(len(Q_matrix)):
            Q_matrix[i].add_Q_to_nex(os.path.join(sum_dir, 'trained_models_all.nex'))
        Q_matrix[-1].add_Q_to_nex(os.path.join(sum_dir, 'trained_models_last.nex'))
        shutil.copy(os.path.join(result_dir, 'log.md'), os.path.join(sum_dir, 'logfiles', '{}_log.md'.format(os.path.basename(result_dir))))
        phylum_name = extract_phylum_name(result_dir)
        # Write the phylum name to the destination file
        with open(os.path.join(sum_dir, 'phylum_list.txt'), 'a') as f:
            f.write(phylum_name + '\n')

def filter_directories(root_directory, regex):
    filtered_directories = []
    for directory in os.listdir(root_directory):
        full_directory = os.path.join(root_directory, directory)
        if os.path.isdir(full_directory) and re.match(regex, directory):
            filtered_directories.append(full_directory)
    return filtered_directories

def integrate_phylogenetic_models(directory_list, sum_dir='./summary'):
    # Create the treefiles & logfiles directory if it doesn't exist
    treefiles_dir = os.path.join(sum_dir, 'treefiles')
    if not os.path.exists(treefiles_dir):
        os.makedirs(treefiles_dir)
    logfiles_dir = os.path.join(sum_dir, 'logfiles')
    if not os.path.exists(logfiles_dir):
        os.makedirs(logfiles_dir)
    
    for directory in directory_list:
        process_directory(directory, sum_dir)

def plot_model(existed_model_nex, trained_model_nex, sum_res):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)

    pca_script = os.path.join(parent_dir, "PCA_Q.R")
    tsne_script = os.path.join(parent_dir, "tSNE_Q.R")

    subprocess.run(["Rscript", pca_script, existed_model_nex, trained_model_nex, sum_res])
    subprocess.run(["Rscript", tsne_script, existed_model_nex, trained_model_nex, sum_res])
    subprocess.run(["Rscript", pca_script, "NULL", trained_model_nex, sum_res])
    subprocess.run(["Rscript", tsne_script, "NULL", trained_model_nex, sum_res])

# A simpler version of making distance matrix, which formed as a matrix
# def calculate_distance(nex_file, attr = 'Q_matrix'):
#     # Read nex file and extract all models
#     # This depends on the structure of your nex file and the Model class
#     models = extract_Q_from_nex(nex_file)  # Replace with actual function to read nex file

#     # change the model names to the phylum names
#     for i in range(len(models)):
#         models[i].create_Q_matrix()
#         models[i].model_name = extract_phylum_name(models[i].model_name)
#         models[i].Q_params = models[i].Q_params/np.sum(models[i].Q_params)

#     # Calculate pairwise distance for all models
#     distance_matrix = np.zeros((len(models), len(models)))
#     for i in range(len(models)):
#         for j in range(i, len(models)):
#             attr1 = getattr(models[i], attr)
#             attr2 = getattr(models[j], attr)
#             # corr = np.corrcoef(attr1.flatten(), attr2.flatten())[0, 1]
#             dist = np.linalg.norm(attr1 - attr2)
#             distance_matrix[i, j] = dist
#             distance_matrix[j, i] = dist

#     return distance_matrix, [model.model_name for model in models]  # Assuming each model has a name attribute

# def save_distance_to_csv(distance_matrix, model_names, output_file):
#     # Open the output file in write mode
#     with open(output_file, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)

#         # Write the header
#         writer.writerow(model_names)
#         # Write the rows
#         for i, row in enumerate(distance_matrix):
#             writer.writerow([model_names[i]] + list(row))

# def write_distance_matrix(nex_file, output_file):
#     distance_matrix, model_names = calculate_distance(nex_file)
#     save_distance_to_csv(distance_matrix, model_names, output_file)

# Another version of making distance matrix, which formed as ggplot data format
def calculate_correlation_and_distance(model1, model2):
    # Calculate correlation and Euclidian distance for Q_params, state_freq, and Q_matrix
    if model1.Q_matrix is None:
        model1.create_Q_matrix()
    if model2.Q_matrix is None:
        model2.create_Q_matrix()
    model1.Q_params = model1.Q_params/np.sum(model1.Q_params)
    model2.Q_params = model2.Q_params/np.sum(model2.Q_params)
    correlations = []
    distances = []
    for attr in ['Q_params', 'state_freq', 'Q_matrix']:
        attr1 = getattr(model1, attr)
        attr2 = getattr(model2, attr)
        corr = np.corrcoef(attr1.flatten(), attr2.flatten())[0, 1]
        dist = np.linalg.norm(attr1 - attr2)
        correlations.append(corr)
        distances.append(dist)
    return correlations, distances

def calculate_trained_models_dist(nex_file):
    models = extract_Q_from_nex(nex_file)
    n = len(models)
    correlations = np.zeros((n, n, 3))
    distances = np.zeros((n, n, 3))
    for i in range(n):
        for j in range(i, n):
            correlations[i, j], distances[i, j] = calculate_correlation_and_distance(models[i], models[j])
            correlations[j, i], distances[j, i] = correlations[i, j], distances[i, j]
    return correlations, distances, [model.model_name for model in models]

def calculate_all_models_dist(trained_nex_file, existed_nex_file):
    trained_models = extract_Q_from_nex(trained_nex_file)
    existed_models = extract_Q_from_nex(existed_nex_file)
    n, m = len(trained_models), len(existed_models)
    correlations = np.zeros((n, m, 3))
    distances = np.zeros((n, m, 3))
    for i in range(n):
        for j in range(m):
            correlations[i, j], distances[i, j] = calculate_correlation_and_distance(trained_models[i], existed_models[j])
    return correlations, distances, [model.model_name for model in trained_models], [model.model_name for model in existed_models]

def save_to_csv(correlations, distances, model_names1, model_names2, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['model1', 'model2', 'Q_params correlation', 'state_freq correlation', 'Q_matrix correlation', 'Q_params distance', 'state_freq distance', 'Q_matrix distance'])
        for i in range(correlations.shape[0]):
            for j in range(correlations.shape[1]):
                writer.writerow([model_names1[i], model_names2[j]] + correlations[i, j].tolist() + distances[i, j].tolist())

def main(root_directory, sum_dir, regex, existed_model_nex):
    trained_model_nex = os.path.join(sum_dir, 'trained_models_last.nex')
    if not os.path.exists(sum_dir):
        os.makedirs(sum_dir)

    filtered_directories = filter_directories(root_directory, regex)
    integrate_phylogenetic_models(filtered_directories, sum_dir)
    plot_model(existed_model_nex, trained_model_nex, sum_dir)

    correlations, distances, model_names = calculate_trained_models_dist(trained_model_nex)
    save_to_csv(correlations, distances, model_names, model_names, os.path.join(sum_dir, 'trained_models_dist.csv'))
    correlations, distances, model_names1, model_names2 = calculate_all_models_dist(trained_model_nex, existed_model_nex)
    save_to_csv(correlations, distances, model_names1, model_names2, os.path.join(sum_dir, 'all_models_dist.csv'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', help='Input root directory', required=True)
    parser.add_argument('-o', '--output', help='Output directory',default='./summary')
    parser.add_argument('-r', '--regex', help='Regex pattern', default='.*')
    parser.add_argument('-n', '--nex', help='Path to existed model.nex', required=True)

    args = parser.parse_args()

    main(args.input, args.output, args.regex, args.nex)