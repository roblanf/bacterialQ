import numpy as np
import os

class SequenceData:
    def __init__(self, aln, names):
        self.aln = aln
        self.names = names
        self.pis_mask = self.calculate_pis_mask()

    def calculate_pis_mask(self):
        array = self.aln.copy()
        array[array == '-'] = np.nan
        def func(column):
            _, counts = np.unique(column, return_counts=True)
            return np.sum(counts >= 2) >= 2
        pis_mask = np.apply_along_axis(func, 0, array)
        return pis_mask

    def filter_array(self, nchar_row=4, nchar_col=1):
        row_mask = np.sum(self.aln != '-', axis=1) >= nchar_row
        self.aln = self.aln[row_mask]
        self.names = self.names[row_mask]
        col_mask = np.sum(self.aln != '-', axis=0) >= nchar_col
        self.aln = self.aln[:, col_mask]

    def filter_array_with_ratio(self, pct_row, pct_col):
        row_mask = np.sum(self.aln != '-', axis=1) >= pct_row * self.aln.shape[1]
        self.aln = self.aln[row_mask]
        self.names = self.names[row_mask]
        col_mask = np.sum(self.aln != '-', axis=0) >= pct_col * self.aln.shape[0]
        self.aln = self.aln[:, col_mask]

    def keep_array(self, ntaxa=3, npis_site=5):
        num_taxa = self.aln.shape[0]
        num_pis_site = np.sum(self.pis_mask)
        return num_taxa >= ntaxa and num_pis_site >= npis_site

    def array_to_fasta(self, fasta_file):
        with open(fasta_file, 'w') as file:
            for i in range(self.aln.shape[0]):
                file.write(f">{self.names[i]}\n")
                file.write("".join(self.aln[i]) + "\n")

    def get_taxa_list(self):
        return list(self.names)

    def get_gap_ratio(self):
        return np.sum(self.aln == '-') / self.aln.size

def fasta_to_array(fasta_file):
    sequences = []
    names = []
    with open(fasta_file, 'r') as file:
        seq = ""
        for line in file:
            if line.startswith('>'):
                if seq:
                    sequences.append(list(seq))
                    seq = ""
                names.append(line.strip()[1:])
            else:
                seq += line.strip()
        if seq:
            sequences.append(list(seq))
    
    seq_lengths = [len(seq) for seq in sequences]
    if len(set(seq_lengths)) != 1:
        raise ValueError("Input sequences are not aligned.")
    
    return SequenceData(np.array(sequences), np.array(names))
    
def drop_rubbish_aln(alignment_file, nchar_row=4, nchar_col=1, ntaxa=3, npls_site=5, auto_drop=True):
    if os.path.exists(alignment_file):
        if os.path.getsize(alignment_file) == 0:
            if auto_drop:
                os.remove(alignment_file)
            return False
    else:
        return False
    sequence_data = fasta_to_array(alignment_file)
    sequence_data.filter_array(nchar_row, nchar_col)
    if_keep = sequence_data.keep_array(ntaxa, npls_site)
    
    if if_keep:
        sequence_data.array_to_fasta(alignment_file)
    elif auto_drop:
        os.remove(alignment_file)
    
    return if_keep