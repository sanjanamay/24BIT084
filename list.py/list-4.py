import random

numbers = [random.randint(-50, 50) for _ in range(30)]
print("Original list of 30 numbers:", numbers)

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
