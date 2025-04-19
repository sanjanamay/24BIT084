def remove_substring(onestring, removestring):
    return onestring.replace(removestring, "")
onestring = input("Enter the main string: ")
removestring = input("Enter the substring to remove: ")
finalstring = remove_substring(onestring, removestring)
print("Final string:", finalstring)
