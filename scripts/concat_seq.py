#!/usr/bin/env python3
import os
import sys
from Bio import SeqIO

def process_fasta_file(filepath, sequences):
    """
    Process a single FASTA file and update the sequences dictionary.
    Args:
        filepath (str): Path to the FASTA file.
        sequences (dict): Dictionary to store sequences for each species.
    """
    for record in SeqIO.parse(filepath, "fasta"):
        species_id = record.id.split('_')[0]
        if species_id in sequences:
            sequences[species_id] += str(record.seq)
        else:
            sequences[species_id] = str(record.seq)

def concatenate_seq_dict(input_dir, output_file, recursive=False):
    """
    Concatenate sequences from FASTA files in a directory.
    Args:
        input_dir (str): Path to the input directory.
        output_file (str): Path to the output file.
        recursive (bool): Whether to search directories recursively.
    """
    sequences = {}

    def handle_directory(directory):
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isdir(filepath) and recursive:
                handle_directory(filepath)
                print("Recursive on sub-folder")
            elif filename.endswith(".faa"):
                process_fasta_file(filepath, sequences)

    handle_directory(input_dir)

    with open(output_file, 'w') as f:
        for species_id, sequence in sequences.items():
            f.write(f">{species_id}\n{sequence}\n")

def concatenate_seq_list(file_list, output_file):
    """
    Concatenate sequences from a list of FASTA file paths.
    Args:
        file_list (list): List of file paths.
        output_file (str): Path to the output file.
    """
    sequences = {}

    for filepath in file_list:
        filepath_str = str(filepath)  # Covert to string in case of Path object
        if filepath_str.endswith(".faa"):
            process_fasta_file(filepath_str, sequences)

    with open(output_file, 'w') as f:
        for species_id, sequence in sequences.items():
            f.write(f">{species_id}\n{sequence}\n")


def main():
    # Usage: python script.py input_directory output_file recursive
    input_dir = sys.argv[1]
    output_file = sys.argv[2]
    recursive = False if len(sys.argv) < 4 else sys.argv[3].lower() == 'true'

    concatenate_sequences(input_dir, output_file, recursive)

if __name__ == "__main__":
    main()
