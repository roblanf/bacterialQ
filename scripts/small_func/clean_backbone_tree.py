#!/usr/bin/env python3
import re
import sys

def replace_text_in_quotes(file_name, drop_support_value=False):
    with open(file_name, 'r') as file:
        text = file.read()

    pattern = r"'[^']*'"
    matches = re.findall(pattern, text)
    
    for match in matches:
        parts = match.strip("'").split(';')
        for part in parts:
            if drop_support_value:
                if ':' in part:
                    replacement = part.split(':')[1].split(';')[0].strip()
            else:
                replacement = "'" + part.split(';')[0].strip() + "'"
            text = text.replace(match, replacement)
    
    return text

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    drop_support_value = sys.argv[3].lower() == 'false' if len(sys.argv) > 3 else True

    result = replace_text_in_quotes(input_file, drop_support_value)
    write_to_file(output_file, result)

if __name__ == "__main__":
    main()
