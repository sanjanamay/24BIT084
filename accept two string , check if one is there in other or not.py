def check_substring(main_string, sub_string):
    if sub_string in main_string:
        return True
    else: 
        return False

# Accept two strings
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to check: ")

if check_substring(main_string, sub_string):
    print(f"The string '{sub_string}' is found in '{main_string}'.")
else:
    print(f"The string '{sub_string}' is not found in '{main_string}'.")
