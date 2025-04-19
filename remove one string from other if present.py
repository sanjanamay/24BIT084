def remove_substring(main_string, remove_string):
    index = main_string.find(remove_string)
    if index != -1:
        # If the substring is found, remove it
        return main_string[:index] + main_string[index + len(remove_string):]
    return main_string  # Return the original string if not found


main_string = input("Enter the main string: ")
remove_string = input("Enter the string to remove: ")

final_string = remove_substring(main_string, remove_string)
print("Final string:", final_string)
