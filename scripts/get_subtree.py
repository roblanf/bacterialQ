#!/usr/bin/env python3
import os
import argparse
from Bio import Phylo
import copy

def prune_tree(tree_file, taxa_list_path, output_file):
    # Read newick to prune
    tree = Phylo.read(tree_file, "newick")

    # Read list of taxa to subset
    taxa_list = read_taxa_list(taxa_list_path)

    subtree = get_subtree(tree, taxa_list)

    # Check number of subtree tips == number of taxa
    assert len([tip for tip in subtree.get_terminals()]) == len(set(taxa_list))

    print(f"Pruned tree saved to {output_file}")
    Phylo.write(subtree, output_file, "newick")

def read_taxa_list(path_to_list):
    if os.path.isfile(path_to_list):
        with open(path_to_list, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    elif os.path.isdir(path_to_list):
        taxa_list = []
        for file in os.listdir(path_to_list):
            file_path = os.path.join(path_to_list, file)
            if os.path.isfile(file_path):
                with open(file_path, "r") as f:
                    taxa_list.extend([line.strip() for line in f.readlines() if line.strip()])
        return taxa_list
    else:
        raise ValueError(f"{path_to_list} is neither a file nor a directory.")

def get_subtree(tree, taxa_list):
    cptree = copy.deepcopy(tree)
    for tip in cptree.get_terminals():
        if tip.name not in taxa_list:
            cptree.prune(tip)
    return cptree

def get_taxa_list_from_fasta(fasta_file):
    species_list = []
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):  # headers start with '>'
                species_name = line.split(' ')[0][1:].strip()
                species_list.append(species_name)
    return species_list

def get_subtree_from_fasta(tree, fasta_file, output_file):
    species_list = get_taxa_list_from_fasta(fasta_file)
    subtree = get_subtree(tree, species_list)
    Phylo.write(subtree, output_file, "newick")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prune a tree based on a list of taxa.")
    parser.add_argument("tree_file", help="Path to the input tree file (in newick format).")
    parser.add_argument("taxa_list_path", help="Path to the taxa list file or directory.")
    parser.add_argument("output_file", help="Path to the output file for the pruned tree.")
    
    args = parser.parse_args()
    
    prune_tree(args.tree_file, args.taxa_list_path, args.output_file)