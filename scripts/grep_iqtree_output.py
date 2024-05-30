#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re
import os

def plot_loci_statistic(iqtree_result_path, output_path):
    """
    This function creates a scatter plot of the proportion of informative sites against the number of sites.
    It also creates a histogram of the proportion of informative sites on the right side of the scatter plot.

    Parameters:
    iqtree_result_path (str): The path to the IQ-TREE result file.
    output_path (str): The path where the plot will be saved.

    Returns:
    None
    """
    with open(iqtree_result_path, 'r') as file:
        lines = file.readlines()

    # Find the start and end of the data block
    start_index = lines.index("  ID\tType\tSeq\tSite\tUnique\tInfor\tInvar\tConst\tName\n")
    end_index = lines.index("Column meanings:\n")

    # Extract the data block
    data_block = lines[start_index:end_index]

    # Parse the data using csv.reader
    reader = csv.DictReader(data_block, delimiter='\t')

    # Calculate the proportions
    infor_prop = []
    site = []
    for row in reader:
        infor_site_value = float(row['Infor']) / float(row['Site'])
        infor_prop.append(infor_site_value)
        site.append(float(row['Site']))

    # Create the scatter plot
    fig = plt.figure(figsize=(8, 6))  # Change the figure size to make it square
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
    ax_main = plt.subplot(gs[0, 0])
    ax_yDist = plt.subplot(gs[0, 1], sharey=ax_main)

    # the scatter plot:
    ax_main.scatter(site, infor_prop, alpha=0.5)

    # histograms
    ax_yDist.hist(infor_prop, bins=20, orientation='horizontal', align='mid', rwidth=0.7, color='gray', edgecolor='black')  # Reduce the bar width

    # labels
    ax_main.set_xlabel('Number of Sites')
    ax_main.set_ylabel('Proportion of Informative Sites')
    ax_main.set_title('Loci Statistics')

    # remove labels on the histograms
    plt.setp(ax_yDist.get_yticklabels(), visible=False)
    ax_yDist.patch.set_alpha(0)

    # Force y-axis to be between 0 and 1
    ax_main.set_ylim(0, 1)
    ax_yDist.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


import re
import csv
import os

def write_iqtree_statistic(iqtree_result_path, result_name, output_path, extra_info=None):
    """
    This function extracts certain statistics from an IQ-TREE result file and writes them to a CSV file.

    Parameters:
    iqtree_result_path (str): The path to the IQ-TREE result file.
    result_name (str): The name of the result, which will be written to the 'result_name' column of the CSV file.
    output_path (str): The path where the CSV file will be saved.
    extra_info (dict): A dictionary containing additional information to be written to the CSV file.

    Returns:
    dict: A dictionary containing the extracted statistics.
    """
    with open(iqtree_result_path, 'r') as file:
        content = file.read()

    iqtree_summarise = {}

    # Extract the required statistics
    patterns = {
        'total_tree_length': r"Total tree length \(sum of branch lengths\): (\d+\.\d+)",
        'internal_tree_length': r"Sum of internal branch lengths: (\d+\.\d+)", 
        'log_likelihood': r"Log-likelihood of the tree: ([-+]?\d*\.\d+|\d+)",
        'log_likelihood_sd': r"Log-likelihood of the tree: .*?\(s.e. ([-+]?\d*\.\d+|\d+)\)",
        'log_likelihood_Unconstrained': r"Unconstrained log-likelihood .*: ([-+]?\d*\.\d+|\d+)",
        'num_free_params': r"Number of free parameters .*: (\d+)",
        'AIC': r"Akaike information criterion \(AIC\) score: ([-+]?\d*\.\d+|\d+)",
        'AICc': r"Corrected Akaike information criterion \(AICc\) score: ([-+]?\d*\.\d+|\d+)",
        'BIC': r"Bayesian information criterion \(BIC\) score: ([-+]?\d*\.\d+|\d+)",
        'cpu_time': r"Total CPU time used: (.+) seconds",
        'wc_time': r"Total wall-clock time used: (.+) seconds"
    }
  
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            iqtree_summarise[key] = float(match.group(1))

    # Add the extra information to the dictionary
    if extra_info is not None:
        iqtree_summarise.update(extra_info)

    fieldnames = ['result_name', 'total_tree_length', 'internal_tree_length', 'log_likelihood', 
                  'log_likelihood_sd', 'log_likelihood_Unconstrained', 'num_free_params', 
                  'AIC', 'AICc', 'BIC', 'cpu_time', 'wc_time']
    if extra_info is not None:
        fieldnames += list(extra_info.keys())

    if not os.path.exists(output_path):
        with open(output_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    with open(output_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        iqtree_summarise['result_name'] = result_name
        writer.writerow(iqtree_summarise)

    return iqtree_summarise