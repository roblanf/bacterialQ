import sys
import os
import re
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
import argparse

PATTREN = re.compile(r'\.(fa|fn).*$', re.IGNORECASE)

def check_integrity(seq_path):
    records = list(SeqIO.parse(seq_path, "fasta"))
    integrity_dict = {rec.id: round((len(rec.seq) - str(rec.seq).count("-")) / len(rec.seq), 2) for rec in records}
    df = pd.DataFrame.from_dict(integrity_dict, orient='index', columns=[os.path.basename(seq_path)])
    return df

def check_integrity_dic(dic_path):
    pattern = PATTREN
    seq_files = [f for f in os.listdir(dic_path) if pattern.search(f)]
    df = pd.DataFrame()
    for seq_file in seq_files:
        seq_path = os.path.join(dic_path, seq_file)
        df = df.join(check_integrity(seq_path), how='outer')
    return df

def append_alignment(integrity_df, aln_path):
    aln_df = check_integrity_dic(aln_path)
    appended_df = integrity_df.join(aln_df, how='outer')
    return appended_df

def integrity_statistic(df):
    dfc = df.copy()
    numeric_columns = dfc.select_dtypes(include=["float64"]).columns
    rank_column = "info_rank"
    if rank_column in numeric_columns:
        numeric_columns = numeric_columns.drop(rank_column)
    q_50 = dfc[numeric_columns].quantile(0.5)
    dfc.loc[:, 'q50_freq'] = (dfc[numeric_columns] < q_50).mean(axis=1).round(2)
    dfc.loc[:, 'avg_integrity'] = dfc[numeric_columns].mean(axis=1).round(2)
    dfc.loc[:, 'empty_freq'] = (dfc[numeric_columns] == 0).mean(axis=1).round(2)
    return dfc

def combine_ref_info(ref_path, integrity_df):
    ref_df = pd.read_csv(ref_path, sep='\t')
    original_ref_columns = ref_df.columns.tolist()
    ref_df = ref_df[ref_df['ID'].isin(integrity_df.index)]
    combined_df = pd.merge(ref_df, integrity_df, left_on="ID", right_index=True, how="left")
    
    # Reorder the columns so that the original columns from ref_df are at the front
    new_columns = [col for col in combined_df.columns if col not in original_ref_columns]
    reordered_columns = original_ref_columns + new_columns
    combined_df = combined_df[reordered_columns]
    
    return combined_df

def analysis_integrity(combined_df, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot histogram for 'Average Integrity'
    combined_df['avg_integrity'].plot.hist(ax=ax1, bins=20, edgecolor='black')
    ax1.set_title("Average Integrity")
    
    # Plot histogram for 'Empty Frequency'
    combined_df['empty_freq'].plot.hist(ax=ax2, bins=20, edgecolor='black')
    ax2.set_title("Empty Frequency")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "quality_check.png"))
    plt.close()


def generate_combined_df(train_loc_path, test_loc_path, taxa_file, output_dir):
    train_df = check_integrity_dic(train_loc_path)
    test_df = check_integrity_dic(test_loc_path)
    integrity_df = train_df.join(test_df, how='outer')
    combined_df = combine_ref_info(taxa_file, integrity_df)
    combined_df.to_csv(os.path.join(output_dir, "combined_df.csv"), index=False)

    return combined_df

def analysis_on_spc_taxa_name(combined_df, taxa_scale, taxa_name):
    taxa_scale = taxa_scale.capitalize()
    selected_df = combined_df[combined_df[taxa_scale] == taxa_name]
    selected_df = integrity_statistic(selected_df)
    selected_df.loc[:, "info_rank"] = selected_df['avg_integrity'].rank(ascending=False)
    return selected_df

def shrink_loc(combined_df, t_drop):
    pattern = PATTREN
    selected_columns = [col for col in combined_df.columns if pattern.search(col)]
    loc_to_drop = [col for col in selected_columns if combined_df[col].mean() < t_drop]
    pruned_doc = combined_df.drop(columns=loc_to_drop)
    return pruned_doc

def shrink_species(combined_df, t_drop):
    species_to_drop = combined_df.index[combined_df['avg_integrity'] < t_drop]
    pruned_doc = combined_df.drop(index=species_to_drop)
    return pruned_doc

def quality_trimming(combined_df, taxa_scale, taxa_name, output_dir, t_drop_loc=0.2, t_drop_species=0.5):
    if not isinstance(combined_df, pd.DataFrame):
        combined_df = pd.read_csv(combined_df)
    selected_df = analysis_on_spc_taxa_name(combined_df, taxa_scale, taxa_name)
    
    analysis_integrity(selected_df, output_dir)
    
    pruned_doc = shrink_loc(selected_df, t_drop_loc)
    pruned_doc = integrity_statistic(pruned_doc)
    pruned_doc = shrink_species(pruned_doc, t_drop_species)
    
    pattern = PATTREN
    with open(os.path.join(output_dir, "select_loci.txt"), "w") as f:
        f.write("\n".join([col for col in pruned_doc.columns if pattern.search(col)]))
    with open(os.path.join(output_dir, "select_id.txt"), "w") as f:
        f.write("\n".join(pruned_doc.loc[:,"ID"]))
    
    pruned_doc.to_csv(os.path.join(output_dir, "pruned_integrity_table.csv"), index=False)

def check_empty_seq(file_path):
    """
    Check if a fasta file contains only empty sequences (? or -).

    Args:
        file_path (str): Path to the fasta file.

    Returns:
        bool: True if the file contains only empty sequences, False otherwise.
    """
    for record in SeqIO.parse(file_path, "fasta"):
        seq = str(record.seq).replace("?", "").replace("-", "")
        if seq:
            return False
    return True

def trim_empty_seq(path):
    """
    Recursively trim empty sequences from fasta files in a directory and its subdirectories.

    Args:
        path (str): Path to the directory.
    """
    fasta_pattern = re.compile(r'\.(fa|fn).*$', re.IGNORECASE)

    for root, dirs, files in os.walk(path):
        for file in files:
            if fasta_pattern.search(file):
                file_path = os.path.join(root, file)
                if check_empty_seq(file_path):
                    os.remove(file_path)

def main(args):
    combined_df = pd.read_csv(args.combined_df)
    quality_trimming(combined_df, args.taxa_scale, args.taxa_name, args.output_dir, args.t_drop_loc, args.t_drop_species)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quality trimming for sequence alignments.")
    parser.add_argument("-d", "--combined_df", required=True, help="Path to the reference taxa information file with quality info")
    parser.add_argument("-s", "--taxa_scale", required=True, help="Taxonomic scale for analysis")
    parser.add_argument("-n", "--taxa_name", required=True, help="Taxonomic name for analysis")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory")
    parser.add_argument("-l", "--t_drop_loc", type=float, default=0.2, help="Threshold for dropping loci (default: 0.2)")
    parser.add_argument("-t", "--t_drop_species", type=float, default=0.5, help="Threshold for dropping species (default: 0.5)")
    
    args = parser.parse_args()
    main(args)