#!/usr/bin/env python3
import argparse
import re

def find_remove_positions(tree, level):
    level_prefix = f'{level}__'
    remove_positions = []
    length = len(tree)
    i = 0
    while i < length:
        if tree[i] == "'":
            j = tree.find("'", i + 1)
            if j != -1 and level_prefix in tree[i+1:j]:
                remove_positions.append((i, j+1))
                i = j + 1
            else:
                i += 1
        else:
            i += 1
    return remove_positions

def remove_brackets(tree, remove_positions):
    for start, end in reversed(remove_positions):
        left_count = 0
        right_count = 0
        j = start - 1
        while j >= 0:
            if tree[j] == '(':
                left_count += 1
            elif tree[j] == ')':
                right_count += 1
            if left_count == right_count:
                break
            j -= 1
        tree = tree[:j] + tree[start:end] + tree[end:]
    return tree

def process_tree(input_file, output_file, level):
    with open(input_file, 'r') as file:
        tree = file.read().strip()

    remove_positions = find_remove_positions(tree, level)
    processed_tree = remove_brackets(tree, remove_positions)

    with open(output_file, 'w') as file:
        file.write(processed_tree)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a Newick tree file and output a skeleton tree.')
    parser.add_argument('input_file', help='Input Newick tree file')
    parser.add_argument('output_file', help='Output skeleton tree file')
    parser.add_argument('level', choices=['p', 'c', 'o', 'f', 'g', 's'],
                        help='Taxonomic level to retain (p: phylum, c: class, o: order, f: family, g: genus, s: species)')

    args = parser.parse_args()

    level_map = {'p': 'p', 'c': 'c', 'o': 'o', 'f': 'f', 'g': 'g', 's': 's'}
    level = level_map[args.level]

    process_tree(args.input_file, args.output_file, level)