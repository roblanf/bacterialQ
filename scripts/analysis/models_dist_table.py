#!/usr/bin/env python3
import numpy as np
import csv
import sys
import os
import argparse
file_path = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(file_path)))

from Q_convert import *

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

def main():
    parser = argparse.ArgumentParser(description='Calculate and save model correlations and distances.')
    parser.add_argument('trained_nex_file', type=str, help='Path to the trained .nex file')
    parser.add_argument('existed_nex_file', type=str, help='Path to the existed .nex file')
    args = parser.parse_args()

    correlations, distances, model_names = calculate_trained_models_dist(args.trained_nex_file)
    save_to_csv(correlations, distances, model_names, model_names, 'trained_models_dist.csv')
    correlations, distances, model_names1, model_names2 = calculate_all_models_dist(args.trained_nex_file, args.existed_nex_file)
    save_to_csv(correlations, distances, model_names1, model_names2, 'all_models_dist.csv')

if __name__ == '__main__':
    main()