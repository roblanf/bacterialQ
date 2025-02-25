def compare_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Compare the first line with the last line
    if lines[0].strip() == lines[-1].strip():
        print("The first line is the same as the last line.")
    else:
        print("The first line is different from the last line.")
    
    # Compare each line with the previous line
    for i in range(1, len(lines)):
        if lines[i].strip() == lines[i-1].strip():
            print(f"Line {i+1} is the same as line {i}.")
        else:
            print(f"Line {i+1} is different from line {i}.")

# Example usage
file_path = '/home/tim/project/bacterialQ/Result_nova/extend_global_model_test/tests/ml.log'
compare_lines(file_path)
