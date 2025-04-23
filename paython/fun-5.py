import string
def ispangram(input_string):
    alphabet_set = set(string.ascii_lowercase)
    input_set = set(input_string.lower())
    return alphabet_set <= input_set
test_strings = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels"
]
for sentence in test_strings:
    if ispangram(sentence):
        print(f"'{sentence}' is a pangram.")
    else:
        print(f"'{sentence}' is not a pangram.")
