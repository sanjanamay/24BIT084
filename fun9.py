def count_alpha_digits(text):
    counts = {"alphabets": 0, "digits": 0}
    for char in text:
        if char.isalpha():
            counts["alphabets"] += 1
        elif char.isdigit():
            counts["digits"] += 1
    return counts

text = "welcome147sanjana567"
print(count_alpha_digits(text))
