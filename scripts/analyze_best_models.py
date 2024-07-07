import re
import argparse
from collections import defaultdict

def count_models(model_list):
    """
    Count the occurrences of each model in the list.
    """
    model_count = defaultdict(int)
    for model in model_list:
        model_count[model] += 1
    return model_count

def extract_models(file, detailed=False):
    """
    Extract the models of alignment from the Nexus file.
    """
    models = []
    extract = False
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'charpartition mymodels =' in line:
                extract = True
                continue
            if extract:
                if 'end;' in line:
                    break
                if line.strip():
                    model = line.split(':')[0].strip()
                    if not detailed:
                        model = model.split('+')[0].strip()
                    else:
                        model = re.sub(r'\{[0-9.,]+\}', '', model)
                    models.append(model)
        return models

def print_model_counts(model_count, output_file):
    """
    Print the model counts in the specified format.
    """
    with open(output_file, 'w') as f:
        for model, count in sorted(model_count.items(), key=lambda item: item[1], reverse=True):
            f.write(f"{count} {model}\n")

def get_and_print_model_counts(file, output_file, detailed=False):
    """
    Extract the models from the Nexus file, count them, and print the results.
    """
    models = extract_models(file, detailed)
    model_count = count_models(models)
    print_model_counts(model_count, output_file)

    return model_count

def main():
    """
    Main function to parse arguments and process the Nexus file.
    """
    parser = argparse.ArgumentParser(description="Process Nexus file to count model occurrences.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the Nexus file.")
    parser.add_argument('-o', '--output', type=str, required=True, help="Path to the output file.")
    parser.add_argument('-t', '--type', type=str, choices=['simple', 'detailed'], default = "simple", help="Type of model count: 'simple' or 'detailed'.")

    args = parser.parse_args()
    if_detailed = True if args.type == 'detailed' else False
    get_and_print_model_counts(args.file, args.output, detailed = if_detailed)

if __name__ == "__main__":
    main()
