def convert(input_string):
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return ' '.join(sorted_words)
input_string = "banana apple orange apple banana grape cherry orange"
result = convert(input_string)
print("Processed string:", result)
