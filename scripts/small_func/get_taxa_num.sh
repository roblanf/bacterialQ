#!/bin/bash

# Check if command line argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 path_to_fasta_file"
    exit 1
fi

# Get the path to the FASTA file from the command line argument
fasta_file=$1

# Extract species names
species=$(grep "^>" $fasta_file | cut -d " " -f 1 | sed 's/>//g')

# Calculate the number of species
species_count=$(echo "$species" | sort | uniq | wc -l)

# Print the number of species
echo "Number of species: $species_count"

# Print the first ten species names
echo "$species" | head -10