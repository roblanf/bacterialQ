import os
import argparse
from Bio import Phylo
import copy
from io import StringIO

def prune_tree(tree_file, taxa_file_list, output_file):
    # Read newick to prune
    tree = Phylo.read(tree_file, "newick")

    # Read list of taxa to subset
    taxa_list = read_taxa_file(taxa_file_list)

    subtree = get_subtree(tree, taxa_list)
    subtree = prune_degree_one_nodes(subtree.root)

    # Check number of subtree tips == number of taxa
    assert len([tip for tip in subtree.get_terminals()]) == len(set(taxa_list))

    print(f"Pruned tree saved to {output_file}")
    Phylo.write(subtree, output_file, "newick")

def read_taxa_file(paths):
    taxa_list = []
    for path in paths:
        if os.path.isfile(path):
            with open(path, "r") as f:
                taxa_list.extend([line.strip() for line in f.readlines() if line.strip()])
        else:
            raise ValueError(f"{path} is not a valid file path.")

    return taxa_list

def get_subtree(tree, taxa_list):
    cptree = copy.deepcopy(tree)
    taxa_set = set(taxa_list)  # Convert list to set for faster lookup
    # Check if the tree has any terminals
    if not cptree.get_terminals():
        raise ValueError("The tree has no terminals to prune.")
    for tip in cptree.get_terminals():
        if tip.name not in taxa_set:
            cptree.prune(tip)  # Prune the tip if it's not in the taxa set
    cptree = prune_degree_one_nodes(cptree.root)
    # Check if any terminals remain in the tree
    if not cptree.get_terminals():
        raise ValueError("All terminals have been pruned from the tree.")
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

def count_nodes_and_tips(tree):
    """
    Count the number of nodes and tips in a Newick tree string.

    Args:
        tree (str): A Newick tree string.

    Returns:
        tuple: A tuple containing the number of nodes and the number of tips.
    """
    nodes = tree.count('(')
    tips = tree.count(',') + 1
    return nodes, tips

def remove_redundant_nodes(tree_path, output_file=None):
    """
    Check each tree of the Newick tree file for redundant nodes.
    The method is to remove all nodes with degree 1, including potential extra degree 1 root nodes.
    If output_file is provided, write the Newick tree to the output file, otherwise, overwrite the input file.

    Args:
        tree_path (str): The path to the Newick tree file.
        output_file (str, optional): The path to the output file. If not specified, the input file will be overwritten.

    Returns:
        None: The function modifies the tree file in place or writes to the specified output file.
    """
    # Read the tree file
    with open(tree_path, 'r') as file:
        tree_lines = file.readlines()

    modified_lines = []
    for tree_data in tree_lines:
        tree_data = tree_data.strip()

        # Read the tree from the Newick string
        tree = Phylo.read(StringIO(tree_data), "newick")

        # Prune degree 1 nodes
        tree = prune_degree_one_nodes(tree.root)

        # Convert the tree back to Newick string
        output = StringIO()
        Phylo.write(tree, output, "newick")
        modified_lines.append(output.getvalue().strip())

    # Determine the output file path
    output_path = output_file if output_file else tree_path

    # Write the modified tree data to the output file
    with open(output_path, 'w') as file:
        file.write('\n'.join(modified_lines) + '\n')
        
def prune_degree_one_nodes(clade, combine_node_label=False):
    """
    Recursively prune nodes with degree 1 and merge branch lengths.

    Args:
        clade (Bio.Phylo.BaseTree.Clade): The clade to prune.
        combine_node_label (bool): If True, combine the labels of pruned nodes with their child nodes.

    Returns:
        Bio.Phylo.BaseTree.Clade: The pruned clade.
    """
    if clade.is_terminal():
        return clade

    new_clades = []
    for subclade in clade.clades:
        if subclade.is_terminal():
            new_clades.append(subclade)
        else:
            pruned_subclade = prune_degree_one_nodes(subclade, combine_node_label)
            if pruned_subclade and len(pruned_subclade.clades) > 1:
                new_clades.append(pruned_subclade)
            elif pruned_subclade and len(pruned_subclade.clades) == 1:
                # Merge branch lengths and add the single subclade
                single_subclade = pruned_subclade.clades[0]
                single_subclade.branch_length = (single_subclade.branch_length or 0) + (pruned_subclade.branch_length or 0)
                
                # Combine node labels if the flag is set
                if combine_node_label:
                    if pruned_subclade.name:
                        if single_subclade.name:
                            single_subclade.name = f"{pruned_subclade.name}-{single_subclade.name}"
                        else:
                            single_subclade.name = pruned_subclade.name

                new_clades.append(single_subclade)
    clade.clades = new_clades

    # Check if the root node itself is a degree-one node
    # if len(clade.clades) == 1:
    #     single_subclade = clade.clades[0]
    #     single_subclade.branch_length = (single_subclade.branch_length or 0) + (clade.branch_length or 0)
        
    #     # Combine node labels if the flag is set
    #     if combine_node_label:
    #         if clade.name:
    #             if single_subclade.name:
    #                 single_subclade.name = f"{clade.name}-{single_subclade.name}"
    #             else:
    #                 single_subclade.name = clade.name

    #     return single_subclade

    return clade

def root_at_outgroups(tree_file, outgroup_taxa_list, output_file, delete_outgroup=True):
    """
    Roots the tree with the specified species list and optionally prunes the outgroup.

    Args:
        tree_file (str): Path to the Newick tree file.
        outgroup_taxa_list (list): List of outgroup species to root the tree with.
        output_file (str): Path to save the output tree.
        delete_outgroup (bool): Whether to delete the outgroup from the tree.

    Returns:
        None
    """
    trees = Phylo.parse(tree_file, "newick")
    output_trees = []

    for tree in trees:
        # Get the list of taxa in the current tree
        tree_taxa = {leaf.name for leaf in tree.get_terminals()}
        # Find the intersection of outgroup_taxa_list and tree_taxa
        current_outgroup_taxa = list(set(outgroup_taxa_list) & tree_taxa)

        if not current_outgroup_taxa:
            print("No common outgroup taxa found, root the tree at the midpoint.")
            try:
                tree.root_at_midpoint()
            except UnboundLocalError:
                pass
        else:
            try:
                clade = tree.common_ancestor(current_outgroup_taxa)
                clade_species = {leaf.name for leaf in clade.get_terminals()}

                if clade_species == set(current_outgroup_taxa):
                    print("The outgroup clade is monophyletic, root the tree with this clade.")
                    tree.root_with_outgroup(clade)
                else:
                    if len(clade_species) - len(current_outgroup_taxa) == 1:
                        print("The outgroup clade contains one additional taxon, use it as the root.")
                        outgroup_taxa = clade_species - set(current_outgroup_taxa)
                        tree.root_with_outgroup(outgroup_taxa)
                    else:
                        print("The outgroup clade isn't monophyletic, root the tree at the midpoint.")
                        try:
                            tree.root_at_midpoint()
                        except UnboundLocalError:
                            pass
            except ValueError:
                print("The common ancestor clade does not exist, root the tree at the midpoint.")
                try:
                    tree.root_at_midpoint()
                except UnboundLocalError:
                    pass

        if delete_outgroup:
            for taxon in current_outgroup_taxa:
                try:
                    tree.prune(taxon)
                except ValueError:
                    print(f"Taxon {taxon} not found in the tree, skipping pruning for this taxon.")

        output_trees.append(tree)

    print(f"Rooted and pruned trees saved to {output_file}")
    Phylo.write(output_trees, output_file, "newick")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prune a tree based on a list of taxa.")
    parser.add_argument("tree_file", help="Path to the input tree file (in newick format).")
    parser.add_argument("taxa_list_path", help="Path to the taxa list file or directory.")
    parser.add_argument("output_file", help="Path to the output file for the pruned tree.")
    
    args = parser.parse_args()
    
    prune_tree(args.tree_file, args.taxa_list_path, args.output_file)
