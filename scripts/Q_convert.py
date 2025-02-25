import numpy as np
import os

AA_ORDER = 'ARNDCQEGHILKMFPSTWYV'

class AminoAcidSubstitutionModel:
    def __init__(self, model_name, Q_params, state_freq, if_normalized=False):
        self.model_name = model_name
        self.Q_params = Q_params
        self.state_freq = state_freq
        self.if_normalized = if_normalized
        self.Q_matrix = None
        self.Q_exchange = None

    def create_Q_matrix(self):
        """Create the actual Q matrix from Q_params and state_freq."""
        self.Q_exchange = self.Q_params + self.Q_params.T
        self.Q_matrix = np.copy(self.Q_exchange)
        q_matrix = np.zeros((20, 20))
        for i in range(20):
            for j in range(20):
                if i != j:
                    q_matrix[i, j] = self.state_freq[j] * self.Q_matrix[i, j]
            q_matrix[i, i] = -np.sum(q_matrix[i, :i]) - np.sum(q_matrix[i, i+1:])
        self.Q_matrix = q_matrix
        self.rescale_Q_matrix()

    def rescale_Q_matrix(self):
        """Rescale Q & exchangibility matrix to ensure the average mutation rate is 1."""
        mu = -1 / np.sum(np.diag(self.Q_matrix) * self.state_freq)
        self.Q_matrix *= mu
        self.Q_exchange *= mu
        self.if_normalized = True

    def prepare_for_fasttree(self, transport=True):
        """Prepare Q matrix for FastTree."""
        if self.Q_matrix is None:
            self.create_Q_matrix()
        Q_matrix_fasttree = np.copy(self.Q_matrix)
        if transport:
            Q_matrix_fasttree = np.transpose(Q_matrix_fasttree)
        Q_matrix_fasttree = np.hstack((Q_matrix_fasttree, self.state_freq.reshape(-1, 1)))

        aa_order = AA_ORDER
        Q_matrix_fasttree_str = '\t'.join(list(aa_order)) + "\t" + '*\n'
        for i in range(20):
            row = ['{:.7f}'.format(val) for val in Q_matrix_fasttree[i]]
            Q_matrix_fasttree_str += aa_order[i] + '\t' + '\t'.join(row) + '\n'
        
        return Q_matrix_fasttree_str

    def check_regularity(self):
        """Check regularity of the model."""
        if self.Q_matrix is None:
            self.create_Q_matrix()
        if np.any(self.state_freq <= 0):
            print("Warning: Some amino acids have zero or negative stationary frequency.")
        
        if np.abs(np.dot(self.state_freq, self.Q_matrix)).max() > 1e-7:
            print("Warning: The stationary distribution is not reachable.")
            print(np.dot(self.state_freq, self.Q_matrix))
        
        if not np.allclose(np.dot(np.diag(self.Q_matrix), self.state_freq), -1, atol=1e-7):
            print("Warning: The average rate of mutation is not 1.")
            print(np.dot(np.diag(self.Q_matrix), self.state_freq))
        
        if not np.allclose(np.sum(self.state_freq), 1, atol=1e-7):
            print("Warning: The frequencies of the amino acids do not sum to 1.")
        
        if np.any(np.diag(self.Q_matrix) >= 0):
            print("Warning: Some diagonal elements of the substitution matrix are non-negative.")
        
        if np.any(self.Q_matrix[np.tril_indices(20, -1)] < 0):
            print("Warning: Some off-diagonal elements of the substitution matrix are negative.")
        
        for i in range(20):
            for j in range(i+1, 20):
                if not np.allclose(self.Q_matrix[i, j] / self.Q_matrix[j, i], self.state_freq[j] / self.state_freq[i], atol=1e-7):
                    print("Warning: Time reversibility does not hold for the substitution matrix.")
                    break
    
    def check_precision(self, threshold=1e-7):
        """Check the precision of Q matrix and state frequency vector."""
        if self.Q_matrix is None:
            self.create_Q_matrix()
        q_precision = np.all(np.round(self.Q_matrix, int(-np.log10(threshold))) > 0)
        freq_precision = np.all(np.round(self.state_freq, int(-np.log10(threshold))) > 0)

        if not q_precision:
            print(f"Warning: Q matrix doesn't meet precision requirement (threshold {threshold}).")
        if not freq_precision:
            print(f"Warning: State frequency vector does not meet precision requirement (threshold {threshold}).")

        return q_precision and freq_precision
        
    def export_Q_as_npy(self, dir_path):
        """Export Q matrix and state frequencies as npy files."""
        if self.Q_matrix is None:
            self.create_Q_matrix()
        np.save(os.path.join(dir_path, 'Q_matrix.npy'), self.Q_matrix)
        np.save(os.path.join(dir_path, 'state_freq.npy'), self.state_freq)

    def check_convergence(self, other_model, threshold=0.999):
        """Check convergence between two models."""
        if self.Q_matrix is None:
            self.create_Q_matrix()
        if other_model.Q_matrix is None:
            other_model.create_Q_matrix()

        # Create a mask to exclude diagonal elements
        mask = ~np.eye(self.Q_matrix.shape[0], dtype=bool)

        # Apply the mask and flatten the matrices
        self_flattened = self.Q_matrix[mask]
        other_flattened = other_model.Q_matrix[mask]

        # Calculate the Pearson correlation coefficient between the masked, flattened Q matrices
        corr = np.corrcoef(self_flattened, other_flattened)[0, 1]

        # Calculate the Euclidean distance between the masked, flattened Q matrices
        dist = np.linalg.norm(self_flattened - other_flattened)
        
        # Check if the correlation exceeds the threshold
        if corr > threshold:
            print("Convergence reached")
            return True, corr, dist
        else:
            print("Convergence not reached")
            return False, corr, dist

    def convert_to_fasttree(self, output_dir):
        """Convert the model to FastTree format."""
        if self.Q_matrix is None:
            self.create_Q_matrix()
        # Prepare Q matrix for FastTree
        Q_matrix_fasttree_str = self.prepare_for_fasttree()
        # Check regularity
        self.check_regularity()
        # Get the directory of the input file
        if os.path.splitext(output_dir)[1]:
            # If file_path has an extension, treat it as a file
            output_file_name = output_dir
            print(f"Saving Q matrix for FastTree to {output_file_name}")
        else:
            # If file_path does not have an extension, treat it as a directory
            output_file_name = os.path.join(output_dir, 'Q_matrix_fasttree.txt')
        # Save Q matrix for FastTree
        with open(output_file_name, 'w') as f:
            f.write(Q_matrix_fasttree_str)

    def print_parameter(self):
        """Print parameters of the model."""
        Q_string = ""
        lower_triangle = np.tril(self.Q_params.reshape(20, 20), -1)  # Get the lower triangle of the Q matrix, excluding the diagonal
        for i in range(lower_triangle.shape[0]):
            for j in range(i):
                Q_string += "{:.6f} ".format(lower_triangle[i, j])  # Convert each element to a string and add it to the result string
            Q_string = Q_string.strip() + "\n"  # Remove trailing space and add a newline character
        state_freq_str = " ".join(["{:.6f}".format(i) for i in self.state_freq.flatten()])
        Q_string += state_freq_str  # Add state_freq to the string
        
        return Q_string

    def add_Q_to_nex(self, file_path):
        """Add the model to a nexus file."""
        if not os.path.exists(file_path) or not list_Q_from_nex(file_path):
            # If the file doesn't exist or is empty, create a new file
            with open(file_path, 'w') as f:
                f.write("#nexus;\n\nbegin models;\n\nend;\n")
                
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Find the position to insert the new model
        end_index = lines.index("end;\n")
        
        # Insert the new model
        lines.insert(end_index-1, "\n")
        lines.insert(end_index, f"model {self.model_name}=\n")
        lines.insert(end_index+1, self.print_parameter() + ";\n")

        with open(file_path, 'w') as f:
            f.writelines(lines)

def grep_Q_from_iqtree_format(text):
    """Extract Q_params and state frequencies from IQ-TREE format."""
    matrix_lines = [line for line in text.split('\n') if line.strip()]  # Remove blank lines
    
    # TODO: Check if it's non-rev model and handle accordingly
    if len(matrix_lines[0].split()) == 20:
        return None, None
    
    substitution_params = []
    for i in range(19):
        line = matrix_lines[i].split()
        substitution_params.extend(line)
    
    state_freq = np.array([float(freq.rstrip(';')) for freq in matrix_lines[19].split()])
    
    Q_params = np.zeros((20, 20))
    Q_params[np.tril_indices(20, -1)] = substitution_params
    
    return Q_params, state_freq

def list_Q_from_nex(file_path):
    """List all models in a nexus file."""
    with open(file_path, 'r') as file:
        content = file.read()
    
    if 'begin models;' not in content:
        return []

    models_block = content.split('begin models;')[1].split('end;')[0]
    model_lines = models_block.split('model ')[1:]
    
    model_names = []
    for line in model_lines:
        model_name = line.split('=')[0].strip()
        model_names.append(model_name)
    
    return model_names

def extract_spc_Q_from_nex(file_path, model_name):
    """Extract a specific model from a nexus file."""
    with open(file_path, 'r') as file:
        content = file.read()
    
    models_block = content.split('begin models;')[1].split('end;')[0]
    model_lines = models_block.split('model ')[1:]
    
    for line in model_lines:
        line_model_name = line.split('=')[0].strip()
        if line_model_name.upper() == model_name.upper():  # Name may differ in display and model store
            matrix_str = line.split('=')[1].strip()
            Q_params, state_freq = grep_Q_from_iqtree_format(matrix_str)
            return AminoAcidSubstitutionModel(model_name, Q_params, state_freq)
    
    return None

def extract_Q_from_nex(file_path):
    """Extract all models from a nexus file."""
    model_names = list_Q_from_nex(file_path)
    models = []
    
    for model_name in model_names:
        print(model_name)
        model = extract_spc_Q_from_nex(file_path, model_name)
        if model is not None:
            models.append(model)
    
    return models

def extract_Q_from_iqtree(model_name, file_path):
    """Extract a model from an IQ-TREE file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    start_line = next(i for i, line in enumerate(lines) if "can be used as input for IQ-TREE" in line) + 2
    model_text = '\n'.join([line.strip() for line in lines[start_line:start_line+20]])
    
    Q_params, state_freq = grep_Q_from_iqtree_format(model_text)
    
    return AminoAcidSubstitutionModel(model_name, Q_params, state_freq, False)

def convert_Q_to_fasttree(file_path):
    """Convert a model from IQ-TREE format to FastTree format."""
    # Extract and calculate Q matrix and state frequencies
    model = extract_Q_from_iqtree(None, file_path)
    # Prepare Q matrix for FastTree
    Q_matrix_fasttree_str = model.prepare_for_fasttree()

    # Check regularity
    model.check_regularity()
    # Get the directory of the input file
    dir_path = os.path.dirname(file_path)
    # Save Q matrix and state frequencies
    np.save(os.path.join(dir_path, 'Q_matrix.npy'), model.Q_matrix)
    np.save(os.path.join(dir_path, 'state_freq.npy'), model.state_freq)
    # Save Q matrix for FastTree
    with open(os.path.join(dir_path, 'Q_matrix_fasttree.txt'), 'w') as f:
        f.write(Q_matrix_fasttree_str)

def bubble_plot(model, output_path, bar_freq=True):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import numpy as np
    from matplotlib.lines import Line2D

    aa_order = AA_ORDER

    if model.Q_matrix is None:
        model.create_Q_matrix()
    # Normalize the Q matrix
    model.rescale_Q_matrix()
    Q_norm = model.Q_matrix

    # Create a DataFrame for plotting (lower triangle only, without diagonal)
    df = pd.DataFrame(np.tril(Q_norm, k=-1), index=list(aa_order), columns=list(aa_order))

    # Melt the DataFrame to convert it into a format suitable for scatterplot
    df_melt = df.reset_index().melt(id_vars='index')
    df_melt = df_melt[df_melt['value'] != 0]  # Remove zero values
    df_melt.columns = ['AA1', 'AA2', 'value']

    # Create the bubble plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), gridspec_kw={'height_ratios': [3, 1]})

    sns.scatterplot(data=df_melt, x='AA2', y='AA1', size='value', sizes=(1, 500),
                    ax=ax1, legend=False, color='gray', edgecolor='black', linewidth=1)
    ax1.set_xticks(range(len(aa_order)))
    ax1.set_yticks(range(-1, len(aa_order) - 1))
    ax1.set_xticklabels(list(aa_order), rotation=0, fontsize=12)
    ax1.set_yticklabels(list(aa_order), rotation=0, fontsize=12)
    ax1.set_title(f"Q Matrix: {os.path.basename(model.model_name)}", fontsize=14)
    ax1.tick_params(axis='both', which='both', length=0)  # Remove tick marks

    # Add size legend
    values = np.percentile(df_melt['value'], [10, 50, 75, 90, 100])  # Get 10th, 50th, and 90th percentile values
    labels = [f"{value:.2f}" for value in values]  # Format labels with 2 decimal places
    sizes = (values / np.max(values)) * 500  # Adjust sizes according to your preference
    legend_elements = [Line2D([0], [0], marker='o', color='w', label=label, 
                          markerfacecolor='gray', markersize=np.sqrt(size)) for size, label in zip(sizes, labels)]
    ax1.legend(handles=legend_elements, title='Size', labelspacing=1, frameon=True, loc='upper right', bbox_to_anchor=(0.98, 0.98))

    if bar_freq:
        sns.barplot(x=list(aa_order), y=model.state_freq, ax=ax2, color='white', edgecolor='black')
    else:
        sns.scatterplot(x=list(aa_order), y=[0]*len(aa_order), size=model.state_freq, sizes=(1, 500),
                        ax=ax2, legend=False, color='gray', edgecolor='black', linewidth=1)
    ax2.set_xticks(range(len(aa_order)))
    ax2.set_xticklabels(list(aa_order), rotation=90, fontsize=12)
    ax2.set_ylabel("State Freq", fontsize=12)
    ax2.tick_params(axis='both', which='both', length=0)  # Remove tick marks

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def bubble_difference_plot(prev_model, curr_model, output_path, bar_freq=True, format="amount"):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import numpy as np
    from matplotlib.lines import Line2D

    aa_order = AA_ORDER

    if prev_model.Q_matrix is None:
        prev_model.create_Q_matrix()
    if curr_model.Q_matrix is None:
        curr_model.create_Q_matrix()

    # Calculate the difference between Q matrices
    curr_model.rescale_Q_matrix()
    prev_model.rescale_Q_matrix()
    if format == "percent":
        Q_diff = (curr_model.Q_matrix - prev_model.Q_matrix) / prev_model.Q_matrix
    else:
        Q_diff = curr_model.Q_matrix - prev_model.Q_matrix

    # Ensure the Q_matrix is not the same
    if Q_diff.max() == 0:
        return None

    # Create a DataFrame for plotting (lower triangle only, without diagonal)
    df = pd.DataFrame(np.tril(Q_diff, k=-1), index=list(aa_order), columns=list(aa_order))

    # Melt the DataFrame to convert it into a format suitable for scatterplot
    df_melt = df.reset_index().melt(id_vars='index')
    df_melt = df_melt[df_melt['value'] != 0]  # Remove zero values
    df_melt.columns = ['AA1', 'AA2', 'value']

    # Create the bubble plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9), gridspec_kw={'height_ratios': [3, 1]})

    sns.scatterplot(data=df_melt, x='AA2', y='AA1', size=abs(df_melt['value']), sizes=(1, 500),
                    hue=df_melt['value'] > 0, palette={True: 'white', False: 'black'},
                    ax=ax1, legend=False, edgecolor='black', linewidth=1)
    ax1.set_xticks(range(len(aa_order)))
    ax1.set_yticks(range(-1, len(aa_order) - 1))
    ax1.set_xticklabels(list(aa_order), rotation=0, fontsize=12)
    ax1.set_yticklabels(list(aa_order), rotation=0, fontsize=12)
    if format == "amount":
        ax1.set_title(f"Q Difference: {os.path.basename(prev_model.model_name)} to {os.path.basename(curr_model.model_name)}", fontsize=14)
    else:
        ax1.set_title(f"Q Difference (%): {os.path.basename(prev_model.model_name)} to {os.path.basename(curr_model.model_name)}", fontsize=14)
    ax1.tick_params(axis='both', which='both', length=0)  # Remove tick marks

    # Add size legend
    values = np.percentile(abs(df_melt['value']), [10, 50, 75, 90, 100])  # Get 10th, 50th, and 90th percentile absolute values
    if format == "percent":
        labels_pos = [f"+{int(value * 100)}%" for value in values]  # Format labels as percentages
        labels_neg = [f"-{int(value * 100)}%" for value in values]  # Format labels as percentages
    else:
        labels_pos = [f"+{value:.2f}" for value in values]  # Format labels with 2 decimal places
        labels_neg = [f"-{value:.2f}" for value in values]  # Format labels with 2 decimal places
    sizes = (values / np.max(values)) * 500  # Adjust sizes according to your preference
    legend_elements_pos = [Line2D([0], [0], marker='o', color='w', label=label, 
                          markerfacecolor='white', markeredgecolor='black', markersize=np.sqrt(size)) for size, label in zip(sizes, labels_pos)]
    legend_elements_neg = [Line2D([0], [0], marker='o', color='w', label=label, 
                          markerfacecolor='black', markeredgecolor='black', markersize=np.sqrt(size)) for size, label in zip(sizes, labels_neg)]
    legend_elements = legend_elements_pos + legend_elements_neg
    ax1.legend(handles=legend_elements, title='Size', labelspacing=1, frameon=True, loc='upper right', bbox_to_anchor=(0.98, 0.98))

    if format == "percent":
        freq_diff = (curr_model.state_freq - prev_model.state_freq) / prev_model.state_freq
    else:
        freq_diff = curr_model.state_freq - prev_model.state_freq

    # Function to format y-axis labels as percentages
    def to_percent(y, position):
        return f"{int(y * 100)}%"
    
    if bar_freq:
        sns.barplot(x=list(aa_order), y=freq_diff, ax=ax2, color='white', edgecolor='black')
        if format == "percent":
            ax2.yaxis.set_major_formatter(plt.FuncFormatter(to_percent))
    else:
        sns.scatterplot(x=list(aa_order), y=[0]*len(aa_order), size=abs(freq_diff), sizes=(1, 500),
                        hue=freq_diff > 0, palette={True: 'white', False: 'black'},
                        ax=ax2, legend=False, edgecolor='black', linewidth=1)
    ax2.set_xticks(range(len(aa_order)))
    ax2.set_xticklabels(list(aa_order), rotation=90, fontsize=12)
    ax2.set_ylabel("State Freq Difference", fontsize=12)
    ax2.tick_params(axis='both', which='both', length=0)  # Remove tick marks

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def model_params_to_table(models, data_type):
    """
    Convert a list of AminoAcidSubstitutionModel objects to a DataFrame based on the specified data type.

    Args:
        models (list): List of AminoAcidSubstitutionModel objects.
        data_type (str): Type of data to extract ('state_freq', 'Q_matrix', 'Q_exchange').

    Returns:
        pd.DataFrame: DataFrame containing the specified data from the models.
    """
    import pandas as pd
    aa_order = AA_ORDER

    if data_type == 'state_freq':
        data = {
            'model_name': [model.model_name for model in models],
            **{f'F({aa})': [model.state_freq[i] for model in models] for i, aa in enumerate(aa_order)}
        }
    elif data_type == 'Q_matrix':
        data = {
            'model_name': [model.model_name for model in models]
        }
        for i, aa1 in enumerate(aa_order):
            for j, aa2 in enumerate(aa_order):
                if i != j:
                    data[f'Q({aa1},{aa2})'] = [model.Q_matrix[i, j] for model in models]
    elif data_type == 'Q_exchange':
        data = {
            'model_name': [model.model_name for model in models]
        }
        for i, aa1 in enumerate(aa_order):
            for j, aa2 in enumerate(aa_order):
                if i > j:
                    data[f'R({aa1},{aa2})'] = [model.Q_exchange[i, j] for model in models]
    else:
        raise ValueError("Invalid data_type. Choose from 'state_freq', 'Q_matrix', 'Q_exchange'.")

    return pd.DataFrame(data)

def nexus_to_csv(file_path, data_type, output_path):
    """
    Convert models from a nexus file to a CSV table based on the specified data type and save it to the output path.

    Args:
        file_path (str): Path to the nexus file.
        data_type (str): Type of data to extract ('state_freq', 'Q_matrix', 'Q_exchange').
        output_path (str): Path to save the output CSV file.
    """
    import pandas as pd
    models = extract_Q_from_nex(file_path)
    for model in models:
        model.create_Q_matrix()
    df = model_params_to_table(models, data_type)
    df.to_csv(output_path, index=False)
