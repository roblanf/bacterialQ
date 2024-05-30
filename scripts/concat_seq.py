#!/usr/bin/env python3
import os
import sys
from Bio import SeqIO

def concatenate_sequences(input_dir, output_file, recursive = False):
    # Create a dictionary to store the sequences for each species
    sequences = {}

    # Function to handle the files in a directory
    def handle_directory(directory):
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isdir(filepath) and recursive:
                # If this is a directory and we're doing a recursive search, handle this directory
                handle_directory(filepath)
                print("Recursive on sub-folder")
            elif filename.endswith(".faa"):
                # Parse the FASTA file
                for record in SeqIO.parse(filepath, "fasta"):
                    # Get the species ID from the sequence ID
                    species_id = record.id.split('_')[0]
                    # Append the sequence to the existing sequence for the species, or create a new entry if it doesn't exist
                    if species_id in sequences:
                        sequences[species_id] += str(record.seq)
                    else:
                        sequences[species_id] = str(record.seq)

    # Start handling the input directory
    handle_directory(input_dir)

    # Write the concatenated sequences to the output file
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
