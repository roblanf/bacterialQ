#!/usr/bin/env python3
import numpy as np
import csv
import sys
import os
import argparse
file_path = os.path.realpath(__file__)
sys.path.append(os.path.dirname(os.path.dirname(file_path)))

from Q_convert import *

def calculate_correlation(nex_file):
    # Read nex file and extract all models
    # This depends on the structure of your nex file and the Model class
    models = extract_Q_from_nex(nex_file)  # Replace with actual function to read nex file

    # Calculate pairwise correlation for all models
    correlation_matrix = np.zeros((len(models), len(models)))
    for i in range(len(models)):
        for j in range(i, len(models)):
            correlation = models[i].check_convergence(models[j])[2]  # Assuming check_convergence returns correlation
            correlation_matrix[i, j] = correlation
            correlation_matrix[j, i] = correlation

    return correlation_matrix, [model.model_name for model in models]  # Assuming each model has a name attribute

def save_to_csv(correlation_matrix, model_names, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header
        writer.writerow(model_names)

        # Write the rows
        for i, row in enumerate(correlation_matrix):
            writer.writerow([model_names[i]] + list(row))

def main():
    parser = argparse.ArgumentParser(description='Calculate and save model correlations.')
    parser.add_argument('nex_file', type=str, help='Path to the .nex file')
    parser.add_argument('output_file', type=str, help='Path to the output .csv file')
    args = parser.parse_args()

    correlation_matrix, model_names = calculate_correlation(args.nex_file)
    save_to_csv(correlation_matrix, model_names, args.output_file)

if __name__ == "__main__":
    main()