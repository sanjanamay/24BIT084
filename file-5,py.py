def copy_and_convert(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        content_upper = content.upper()
        outfile.write(content_upper)

    print(f"Contents from '{input_file}' have been copied to '{output_file}' with uppercase conversion.")
input_file = 'source.txt'  
output_file = 'destination.txt'  
copy_and_convert(input_file, output_file)
