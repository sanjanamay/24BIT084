def count_lower_upper(input_string):
    lower_count = 0
    upper_count = 0
    for char in input_string:
        if char.islower():  
            lower_count += 1
        elif char.isupper():  
            upper_count += 1
    return {'lowercase': lower_count, 'uppercase': upper_count}
sample_string = "Hello World!"
result = count_lower_upper(sample_string)
print("Lowercase and Uppercase counts:", result)
