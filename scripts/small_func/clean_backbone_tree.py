#!/usr/bin/env python3
from Bio import Phylo
import sys
import re

def clean_node_name(name, drop_support_value=False):
    """
    Processes a node name by retaining only the part before the first ';' 
    and formatting it according to the user's requirements.
    Optionally drops the support value or includes it in braces.
    """
    if name:
        # Split the name into support value and taxonomic part
        parts = name.split(':')
        support_value = parts[0] if len(parts) > 1 else None
        taxonomic_part = parts[1].split(';')[0].strip() if len(parts) > 1 else parts[0]
        
        if drop_support_value:
            return taxonomic_part  # Return only the taxonomic part
        else:
            return f"{taxonomic_part}{{{support_value}}}"  # Include support value in braces
    return ""

def drop_species_tip(tree, drop_support_value=False):
    """
    Prunes the tree by discarding tips that do not contain '__' in their names.
    Also processes the name of each node to drop the support value if required.
    """
    terminals_to_prune = [leaf for leaf in tree.get_terminals() if '__' not in leaf.name and 'tips' not in leaf.name]

    # Print names of terminals to prune
    print("Terminals to prune:")
    for terminal in terminals_to_prune:
        print(terminal.name)

    # Print names of all terminals in the tree
    print("All terminals in the tree:")
    for terminal in tree.get_terminals():
        print(terminal.name)

    # Prune tips that don't contain '__'
    for terminal in terminals_to_prune:
        tree.prune(terminal)

    # Process names of all nodes
    for node in tree.get_nonterminals() + tree.get_terminals():
        node.name = clean_node_name(node.name, drop_support_value)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    drop_support_value = sys.argv[3].lower() == 'true' if len(sys.argv) > 3 else False

    # Read the tree
    tree = Phylo.read(input_file, 'newick')

    # Prune the tree and process node names
    drop_species_tip(tree, drop_support_value)

    # Write the pruned tree back to a file
    Phylo.write(tree, output_file, 'newick')

if __name__ == "__main__":
    main()