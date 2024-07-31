import sys
import pandas as pd
import re

def read_markdown_file(md_file):
    with open(md_file, 'r') as f:
        content = f.read()
    return content

def extract_last_table(content):
    lines = content.split('\n')
    start_index = None
    end_index = None

    # Corrected regular expression to match the header separator line with at least one '-'
    header_separator_pattern = re.compile(r'^\|(\s*-+\s*\|)+$')

    # Find the start index of the last table
    for i, line in enumerate(lines):
        if header_separator_pattern.match(line):
            start_index = i - 1
            break

    # Find the end index of the last table
    if start_index is not None:
        for i in range(start_index + 2, len(lines)):
            if lines[i].startswith('|'):
                end_index = i
            else:
                break

    if start_index is not None and end_index is not None:
        # Remove the separator line
        table_lines = lines[start_index:end_index + 1]
        table_lines.pop(1)
        return '\n'.join(table_lines)
    else:
        return None

def convert_table_to_dataframe(table):
    rows = table.split('\n')
    header = [col.strip() for col in rows[0].split('|')[1:-1]]
    data = [[col.strip() for col in row.split('|')[1:-1]] for row in rows[1:] if row]
    df = pd.DataFrame(data, columns=header)
    return df

def save_dataframe_to_csv(df, csv_file):
    df.to_csv(csv_file, index=False)

def markdown_to_csv(md_file, csv_file):
    content = read_markdown_file(md_file)
    last_table = extract_last_table(content)
    if last_table is None:
        print('No table found in the Markdown file.')
        return None
    df = convert_table_to_dataframe(last_table)
    save_dataframe_to_csv(df, csv_file)

if __name__ == "__main__":
    markdown_file = sys.argv[1]
    csv_file = sys.argv[2]
    markdown_to_csv(markdown_file, csv_file)