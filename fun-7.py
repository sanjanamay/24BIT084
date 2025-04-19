def ispalindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]
test_strings = [
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "Hello World"
]

for string in test_strings:
    if ispalindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")
