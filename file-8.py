 def remove_words(input_file, output_file):
    # Words to be removed
    words_to_remove = ['a', 'the', 'an']
    
    # Open the input file and output file
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read the content of the input file
        content = infile.read()
        
        # Replace each word in the list with a blank space
        for word in words_to_remove:
            content = content.replace(f' {word} ', ' ')  # Remove surrounded by spaces
            content = content.replace(f' {word}.', '.')  # Handle words ending with a period
            content = content.replace(f' {word},', ',')  # Handle words followed by a comma
            content = content.replace(f'{word} ', ' ')  # Handle word at the start of the sentence
            content = content.replace(f'{word}.', '.')  # Handle word at the end of a sentence

        # Write the modified content to the output file
        outfile.write(content)
    
    print(f"Modified content has been saved to '{output_file}'.")

# File names
input_file = 'input.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your output file name

# Call the function to process the file
remove_words(input_file, output_file)
