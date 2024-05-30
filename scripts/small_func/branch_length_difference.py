#!/usr/bin/env python3

import argparse
from Bio import Phylo
import matplotlib.pyplot as plt

def calculate_relative_difference(tree1, tree2):
    # Parse the trees
    t1 = Phylo.read(tree1, 'newick')
    t2 = Phylo.read(tree2, 'newick')

    # Get the branch lengths
    bl1 = [clade.branch_length for clade in t1.find_clades()]
    bl2 = [clade.branch_length for clade in t2.find_clades()]

    # Calculate the relative differences
    relative_diffs = []
    for b1, b2 in zip(bl1, bl2):
        if b1 is not None and b2 is not None:
            relative_diffs.append((b2 - b1) / ((b1 + b2) / 2))

    return relative_diffs

def plot_relative_difference(relative_diffs):
    # Plot the histogram
    plt.hist(relative_diffs, bins=10, edgecolor='black')
    plt.xlabel('Relative Difference')
    plt.ylabel('Frequency')
    plt.title('Distribution of Relative Differences in Branch Lengths')
    
    # Save the plot to a PNG file and show
    plt.savefig('relative_difference.png')
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Calculate and plot the relative differences in branch lengths between two trees.')
    parser.add_argument('tree1', help='The path to the first Newick tree file.')
    parser.add_argument('tree2', help='The path to the second Newick tree file.')
    args = parser.parse_args()

    relative_diffs = calculate_relative_difference(args.tree1, args.tree2)
    plot_relative_difference(relative_diffs)

if __name__ == '__main__':
    main()