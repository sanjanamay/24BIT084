def count_alpha_digits(input_string):
    alpha_count = 0
    digit_count = 0
    for char in input_string:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():  
            digit_count += 1
    return {'alphabets': alpha_count, 'digits': digit_count}
sample_string = "Hello123 World456"
result = count_alpha_digits(sample_string)
print("Character counts:", result)
