def merge_alternate_lines(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        max_lines = max(len(lines1), len(lines2))
        for i in range(max_lines):
            if i < len(lines1):  
                out.write(lines1[i])
            if i < len(lines2):  
                out.write(lines2[i])

    print(f"Lines have been merged into '{output_file}' successfully."
file1 = 'file1.txt'  
file2 = 'file2.txt'  
output_file = 'merged_file.txt'  
merge_alternate_lines(file1, file2_output_file)
