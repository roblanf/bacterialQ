import os

def create_nexus_partition(input_dir, output_file):
    """
    Creates a NEXUS partition file for IQ-TREE from a directory or list of directories of sequence files.

    Args:
        input_dir (str or list): The directory or list of directories containing sequence files.
        output_file (str): The path to the output NEXUS file.

    Returns:
        None
    """
    # Ensure input_dir is a list
    if isinstance(input_dir, str):
        input_dir = [input_dir]
    
    files = []
    for directory in input_dir:
        files.extend(os.listdir(directory))
    
    with open(output_file, 'w') as f:
        f.write("#nexus\nbegin sets;\n")
        for directory in input_dir:
            for file in os.listdir(directory):
                abs_path = os.path.abspath(os.path.join(directory, file))
                f.write(f"charset {file} = {abs_path}: ;\n")
        f.write("end;\n")