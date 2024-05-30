import os
import random
import itertools
from pathlib import Path
import subprocess
import argparse

def sample_alignment(loci_dir: Path, taxa_list: Path, output_folder: Path, num_aln: int = None, combine_subtree: bool = False, loci_filter: Path = None) -> None:
    output_folder.mkdir(parents=True, exist_ok=True)  # Create the output folder if it doesn't exist

    def filter_loci_files(loci_dir, loci_filter):
        # Get all loci files in the loci directory
        loci_files = [f for f in loci_dir.glob("*.fa*")]
        if loci_filter and loci_filter.stat().st_size > 0:
            # If a loci filter is provided, read the filtered loci and keep only those in the list
            with open(loci_filter, 'r') as f:
                filtered_loci = f.read().splitlines()
            loci_files = [f for f in loci_files if f.name in filtered_loci]
            print(f"Discarded {len([f for f in loci_dir.glob('*.fa*') if f.name not in filtered_loci])} loci based on the loci filter.")
        return loci_files

    def check_empty_seq(file_path):
        # Check if a sequence file contains only empty sequences
        with open(file_path, 'r') as f:
            content = f.read().splitlines()
            for line in content:
                if line.startswith('>'):
                    continue
                if line.strip('-?'):
                    return False
        return True

    def run_faSomeRecords(loci_file, taxa_file, output_file):
        # Run the faSomeRecords command to extract sequences from a loci file based on a taxa file
        cmd = f"faSomeRecords {loci_file} {taxa_file} {output_file}"
        subprocess.run(cmd, shell=True)
        if check_empty_seq(output_file):
            # If the output file contains only empty sequences, remove it and return True
            os.remove(output_file)
            return True
        return False

    def process_loci_files(loci_files, taxa_list, output_dir, num_aln=None):
        splited_aln_count, deleted_aln_count = 0, 0
        if taxa_list.is_file():
            # If a single taxa file is provided
            print(f"Input a single taxa file: {taxa_list}. Sampling sequences for {len(loci_files)} loci.")
            print(f"Number of input species: {sum(1 for line in open(taxa_list))}")
            for loci_file in loci_files:
                output_file = output_dir / os.path.basename(loci_file)
                if run_faSomeRecords(loci_file, taxa_list, output_file):
                    deleted_aln_count += 1
                else:
                    splited_aln_count += 1
        elif taxa_list.is_dir():
            if combine_subtree:
                # If subtrees need to be combined
                print(f"Input {len(os.listdir(taxa_list))} subtree files and combine them. Sampling sequences for {len(loci_files)} loci.")
                all_taxa_file = output_dir / "combined_taxa.txt"
                with open(all_taxa_file, 'w') as f:
                    for taxa_file in os.listdir(taxa_list):
                        if taxa_file.endswith(".txt"):
                            with open(taxa_list / taxa_file, 'r') as tf:
                                f.write(tf.read())
                target_aln_count = min(num_aln or len(loci_files), len(loci_files))
                for loci_file in loci_files:
                    output_file = output_dir / os.path.basename(loci_file)
                    if run_faSomeRecords(loci_file, all_taxa_file, output_file):
                        deleted_aln_count += 1
                    else:
                        splited_aln_count += 1
                    if splited_aln_count >= target_aln_count:
                        break
                if num_aln is not None and splited_aln_count < num_aln:
                    print(f"Could not obtain {num_aln} alignments after combining subtrees. Keeping {splited_aln_count} alignments.")
            else:
                # If subtrees don't need to be combined
                total_aln_count = len(loci_files) * len(os.listdir(taxa_list))
                print(f"Input {len(os.listdir(taxa_list))} subtree files and {len(loci_files)} loci files. Total number of potential alignments: {total_aln_count}.")
                if num_aln is not None and num_aln < total_aln_count:
                    # If the requested number of alignments is less than the total potential alignments
                    print(f"The requested number of alignments ({num_aln}) is less than the total number of potential alignments ({total_aln_count}). Sampling a subset of alignments.")
                    aln_count = 0
                    subtree_loci_pairs = list(itertools.product(
                        (taxa_list / taxa_file for taxa_file in os.listdir(taxa_list) if taxa_file.endswith(".txt")),
                        loci_files
                    ))
                    print(len(subtree_loci_pairs))
                    random.shuffle(subtree_loci_pairs)  # Shuffle the list to avoid sequential selection
                    target_aln_count = min(num_aln or total_aln_count, total_aln_count)
                    target_aln_count = min(int(target_aln_count * 1.1), total_aln_count)  # 10% spare space, but not exceeding total alignment count
                    for taxa_file, loci_file in subtree_loci_pairs[:target_aln_count]:
                        tree_name = os.path.splitext(os.path.basename(taxa_file))[0]
                        loci_name = os.path.splitext(os.path.basename(loci_file))[0]
                        ext = os.path.splitext(loci_file)[1]
                        output_file = output_dir / f"{tree_name}_{loci_name}{ext}"
                        if run_faSomeRecords(loci_file, taxa_file, output_file):
                            deleted_aln_count += 1
                        else:
                            splited_aln_count += 1
                            aln_count += 1
                    if splited_aln_count < num_aln:
                        print(f"Could not obtain the requested {num_aln} alignments. Keeping {splited_aln_count} alignments.")
                else:
                    # If all potential alignments need to be sampled
                    for taxa_file in os.listdir(taxa_list):
                        if taxa_file.endswith(".txt"):
                            tree_name = os.path.splitext(taxa_file)[0]
                            for loci_file in loci_files:
                                loci_name = os.path.splitext(os.path.basename(loci_file))[0]
                                ext = os.path.splitext(loci_file)[1]
                                output_file = output_dir / f"{tree_name}_{loci_name}{ext}"
                                if run_faSomeRecords(loci_file, taxa_list / taxa_file, output_file):
                                    deleted_aln_count += 1
                                else:
                                    splited_aln_count += 1
                    print(f"Obtained {splited_aln_count} alignments from all potential alignments.")
        else:
            raise ValueError(f"{taxa_list} is neither a file nor a directory.")

        print(f"Remaining {splited_aln_count} alignments. Deleted {deleted_aln_count} alignments.")

    loci_files = filter_loci_files(loci_dir, loci_filter)

    if not loci_files:
        raise ValueError("Loci set is empty after filtering. Program will terminate.")

    print("Sampling alignments...")
    process_loci_files(loci_files, taxa_list, output_folder, num_aln=num_aln)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample alignments from loci and subtree directories.")
    parser.add_argument("--loci_dir", type=Path, help="Path to the directory containing loci alignments.")
    parser.add_argument("--taxa_list", type=Path, help="Path to the directory or file containing taxa for each subtree.")
    parser.add_argument("--output_folder", type=Path, help="Path to the output folder.")
    parser.add_argument("-n", "--num_aln", type=int, help="Number of alignments to sample.")
    parser.add_argument("-c", "--combine_subtree", action="store_true", help="Combine subtrees into a single file.")
    parser.add_argument("-f", "--loci_filter", type=Path, help="Path to the file containing the list of loci to filter.")

    args = parser.parse_args()

    sample_alignment(args.loci_dir, args.taxa_list, args.output_folder, args.num_aln, args.combine_subtree, args.loci_filter)