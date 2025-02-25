#!/usr/bin/env python3
# Adapted from get_backbone_tree.py. Addressed the issue arising from taxonomic nesting.
import argparse
import re

# Helper function to find matching left parenthesis for a given right parenthesis
def find_matching_left_parenthesis(tree, right_pos):
    left_count = 0
    right_count = 0
    for i in range(right_pos, -1, -1):
        if tree[i] == ')':
            right_count += 1
        elif tree[i] == '(':
            left_count += 1
        if left_count == right_count:
            return i
    return None

# Function to capture level tags from deleted text
def capture_level_tags(deleted_text, level):
    pattern = re.compile(rf"{level}__([^;\/\']+)")
    return pattern.findall(deleted_text)

# Function to find the removal position of a taxonomic level in the tree
def find_remove_position(tree, level, start_pos):
    level_prefix = f"{level}__"
    i = tree.rfind("'", 0, start_pos)
    while i != -1:
        j = tree.rfind("'", 0, i)
        if j != -1 and level_prefix in tree[j + 1:i]:
            return j, i + 1
        i = tree.rfind("'", 0, j)
    return None

# Function to process the deleted text and return average depth or length (if needed)
def compute_subtree_average_depth(tree):
    """
    Calculate the average tip depth within a given tree, accounting for both terminal tips
    and internal nodes. This function finds all tips and nodes in the tree, calculates their
    branch lengths, and averages them over the number of tips in the entire tree.
    """
    # Capture all terminal tips (tip_name:branch_length) patterns
    tips = re.findall(r'(?<=[(,])[\w\.]+:\d+\.\d+', tree)
    total_tip_depth = 0
    total_tip_count = 0
    
    for tip in tips:
        depth = float(tip.split(':')[-1])
        total_tip_depth += depth
        total_tip_count += 1
    
    # Now handle internal nodes
    total_node_length = 0
    node_tip_count = 0
    
    # Find all closing parentheses and calculate the contribution of internal nodes
    for match in re.finditer(r'\)', tree):
        close_pos = match.start()
        open_pos = find_matching_left_parenthesis(tree, close_pos)
        
        # Find the number of tips (based on commas) inside the node
        subtree_section = tree[open_pos:close_pos]
        ntips_in_node = subtree_section.count(',') + 1
        
        # Find the branch length after this closing parenthesis
        branch_length_match = re.search(r':(\d+\.\d+)', tree[close_pos:])
        if branch_length_match:
            node_length = float(branch_length_match.group(1))
            total_node_length += node_length * ntips_in_node
            node_tip_count += ntips_in_node
    
    # Total tips in the subtree
    ntips_subtree = total_tip_count
    
    if ntips_subtree == 0:
        return 0, 0
    
    # Overall tip depth = terminal tips + internal node contributions
    overall_depth = total_tip_depth + total_node_length
    average_depth = overall_depth / ntips_subtree
    
    return average_depth, ntips_subtree

# Function to remove brackets and process subtree
def remove_brackets(tree, start, end, level, tip_length_strategy):
    # Find the matching left parenthesis
    start_bracket_pos = find_matching_left_parenthesis(tree, start-1)
    deleted_text = tree[start_bracket_pos:start]
    
    # Remove the text inside brackets
    tree = tree[:start_bracket_pos] + tree[start:]
    # Find all level tags within the deleted text
    deleted_tags = capture_level_tags(deleted_text, level)

    if tip_length_strategy != 'none':
        # Process the deleted text and compute average depth based on strategy
        average_depth, ntips = compute_subtree_average_depth(deleted_text)

        if tip_length_strategy == 'default' and average_depth is not None:
            # Update branch length after the current subtree
            match = re.search(r':', tree[start_bracket_pos:])
            if match:
                insert_pos = start_bracket_pos + match.start()
                insertion = f"/{ntips}/{round(average_depth, 4)}"
                tree = tree[:insert_pos] + insertion + tree[insert_pos:]

        # Handle 'add' or 'new' strategy
        elif tip_length_strategy == 'add' and average_depth is not None:
            # Update branch length after the current subtree
            match = re.search(r':(\d+\.\d+)', tree[start_bracket_pos:])
            if match:
                # print(tree[start_bracket_pos + match.start() - 10:start_bracket_pos + match.start()] + "  " + str(ntips) + "  " + str(average_depth))
                branch_length = float(match.group(1))
                updated_length = round(branch_length + average_depth, 9)
                tree = tree[:start_bracket_pos + match.start() + 1] + str(updated_length) + tree[start_bracket_pos + match.end():]

        elif tip_length_strategy == 'new' and average_depth is not None:
            # Add a new node representing the average depth
            new_node = f"({ntips}tips:{round(average_depth, 9)})"
            tree = tree[:start_bracket_pos] + new_node + tree[start_bracket_pos:]

    # Optionally, reinsert deleted tags back into the tree
    if deleted_tags:
        level_prefix = f"{level}__"
        match = re.search(re.escape(level_prefix), tree[start_bracket_pos:])
        if match:
            insertion_pos = re.search(r'[;/\']', tree[start_bracket_pos + match.start():])
            if insertion_pos:
                insertion_pos = insertion_pos.start() + match.start() + start_bracket_pos
                insertion_str = "+".join(deleted_tags)
                tree = tree[:insertion_pos] + f"+{insertion_str}" + tree[insertion_pos:]
    
    return tree, start_bracket_pos

# Function to check the structure of the tree
def check_tree_structure(tree):
    open_parens = tree.count('(')
    commas = tree.count(',')
    if open_parens == (commas - 1) or open_parens == commas:
        return True
    else:
        print(f"Tree structure error: Number of nodes is {open_parens}, while number of tips is {commas}. Ignoring tip length strategy.")
        return False

# Main tree processing function
def process_tree(input_file, output_file, level, tip_length_strategy):
    with open(input_file, 'r') as file:
        tree = file.read().strip()

    # Check the structure of the tree
    if not check_tree_structure(tree):
        tip_length_strategy = 'none'

    start_pos = len(tree) - 1
    while True:
        remove_position = find_remove_position(tree, level, start_pos)
        if not remove_position:
            break

        # Capture the node to process and remove brackets
        tree, new_start_pos = remove_brackets(tree, remove_position[0], remove_position[1], level, tip_length_strategy)
        start_pos = new_start_pos - 1

    with open(output_file, 'w') as file:
        file.write(tree)

# Main argparse setup
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a Newick tree file and output a skeleton tree.')
    parser.add_argument('input_file', help='Input Newick tree file')
    parser.add_argument('output_file', help='Output skeleton tree file')
    parser.add_argument('-l', '--level', choices=['p', 'c', 'o', 'f', 'g', 's'], default='p',
                        help='Taxonomic level to retain (p: phylum, c: class, o: order, f: family, g: genus, s: species)')

    parser.add_argument('-t', '--tip_length_strategy', choices=['default', 'none', 'add', 'new'], default='default',
                        help='Tip length strategy (None: ignore tips, add: add tip branch lengths, new: insert new node for tip lengths)')

    args = parser.parse_args()

    level_map = {'p': 'p', 'c': 'c', 'o': 'o', 'f': 'f', 'g': 'g', 's': 's'}
    level = level_map[args.level]

    process_tree(args.input_file, args.output_file, level, args.tip_length_strategy)


# Here is a test version of the script that uses the Bio.Phylo module to parse the tree
# import argparse
# from Bio import Phylo
# from io import StringIO

# def fold_tree_by_taxonomic_level(input_path, output_path, taxonomic_level):
#     # Read the Newick tree
#     with open(input_path, 'r') as f:
#         newick_str = f.read()
#     tree = Phylo.read(StringIO(newick_str), 'newick')
    
#     def get_taxa_label(label):
#         """Extract support value and taxa string from the node label."""
#         if ":" in label:
#             support_value, taxa_string = label.split(":")
#             return support_value, taxa_string.strip()
#         return None, None

#     def get_taxonomic_group(taxa_string, level):
#         """Extract the specific taxonomic group from the taxa string."""
#         for group in taxa_string.split(';'):
#             group = group.strip()
#             if group.startswith(level):
#                 return group
#         return None

#     def calculate_average_depth(clade, current_depth=0):
#         """Recursively calculate the average depth of all tips under a clade."""
#         if clade.is_terminal():  # Tip node
#             return [(clade, current_depth + clade.branch_length)]
#         depths = []
#         for child in clade.clades:
#             depths.extend(calculate_average_depth(child, current_depth + clade.branch_length))
#         return depths

#     def fold_node(clade, average_depth):
#         """Convert a node into a tip with the same name."""
#         clade.clades = []  # Remove all child nodes
#         clade.branch_length = average_depth  # Set the branch length to the average depth

#     # Traverse the tree and fold nodes by the specified taxonomic level
#     for clade in tree.find_clades():
#         if clade.name:
#             support_value, taxa_string = get_taxa_label(clade.name)
#             if taxa_string:
#                 group = get_taxonomic_group(taxa_string, taxonomic_level)
#                 if group:  # Found a node with the specified taxonomic level
#                     tip_depths = calculate_average_depth(clade)
#                     if tip_depths:
#                         avg_depth = sum(depth for _, depth in tip_depths) / len(tip_depths)
#                         fold_node(clade, avg_depth)
    
#     # Write the modified tree to the output path
#     Phylo.write(tree, output_path, 'newick')
#     print(f"Tree folded at {taxonomic_level} and saved to {output_path}")

# def main():
#     # Set up argument parser
#     parser = argparse.ArgumentParser(description='Fold a Newick tree by a specific taxonomic level.')
#     parser.add_argument('input_path', type=str, help='Path to the input Newick tree file.')
#     parser.add_argument('output_path', type=str, help='Path to save the output folded Newick tree file.')
#     parser.add_argument('taxonomic_level', type=str, help='Taxonomic level to fold at (e.g., "c__" for class).')

#     # Parse the command-line arguments
#     args = parser.parse_args()

#     # Run the fold function with the provided arguments
#     fold_tree_by_taxonomic_level(args.input_path, args.output_path, args.taxonomic_level)

# if __name__ == '__main__':
#     main()
