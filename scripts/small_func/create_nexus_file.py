import os

def create_nexus_partition(input_dir, output_file):
    """
    Creates a NEXUS partition file for IQ-TREE from a directory of sequence files.

    Args:
        input_dir (str): The directory containing sequence files.
        output_file (str): The path to the output NEXUS file.

    Returns:
        None
    """
    files = os.listdir(input_dir)
    with open(output_file, 'w') as f:
        f.write("#nexus\nbegin sets;\n")
        for file in files:
            abs_path = os.path.abspath(os.path.join(input_dir, file))
            f.write(f"charset {file} = {abs_path}: ;\n")
        f.write("end;\n")