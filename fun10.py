def frequency(text):
    words = text.split()
    freq_dict = {word: words.count(word) for word in set(words)}
    return dict(sorted(freq_dict.items()))

# Example usage
text = "duck sparrow pigon duck cuckoo pigon pigon"
print(frequency(text))
