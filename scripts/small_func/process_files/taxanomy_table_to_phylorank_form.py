def convert_taxa_table_format(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove the first line
    lines = lines[1:]

    # Process each line
    processed_lines = []
    for line in lines:
        # Replace the first tab character with '%%%'
        line = line.replace('\t', '%%%', 1)
        processed_lines.append(line)

    # Join the lines back into a single string
    content = ''.join(processed_lines)

    # Replace all tab characters with ';'
    content = content.replace('\t', ';')

    # Replace all '%%%' characters with tab characters
    content = content.replace('%%%', '\t')

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
file_path = '/home/tim/project/bacterialQ/data/r220/rep_bac120_taxonomy_phylorank_formatted.tsv'
convert_taxa_table_format(file_path)