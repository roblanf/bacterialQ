import os
import sys

def read_taxa_from_files_in_folder(folder_path):
    taxa = set()
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                for line in f:
                    taxa.add(line.strip())
    return taxa

def calculate_and_print_taxa_info(folder1, folder2):
    taxa1 = read_taxa_from_files_in_folder(folder1)
    taxa2 = read_taxa_from_files_in_folder(folder2)

    shared_taxa = taxa1.intersection(taxa2)
    only_in_taxa1 = taxa1.difference(taxa2)
    only_in_taxa2 = taxa2.difference(taxa1)

    total_taxa = len(taxa1) + len(taxa2)

    print(f"Shared Taxa: {len(shared_taxa)} ({len(shared_taxa) * 2 / total_taxa * 100:.2f}%)")
    print(f"Only in Folder 1: {len(only_in_taxa1)} ({len(only_in_taxa1) / total_taxa * 100:.2f}%)")
    print(f"Only in Folder 2: {len(only_in_taxa2)} ({len(only_in_taxa2) / total_taxa * 100:.2f}%)")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder1> <folder2>")
        sys.exit(1)

    folder1 = sys.argv[1]
    folder2 = sys.argv[2]

    calculate_and_print_taxa_info(folder1, folder2)

if __name__ == "__main__":
    main()
