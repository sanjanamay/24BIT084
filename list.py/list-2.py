import random

numbers = [random.randint(1, 50) for _ in range(20)]
print("List of 20 random numbers:", numbers)

user_input = int(input("Enter a number to find its positions: "))

positions = [index for index, value in enumerate(numbers) if value == user_input]

if positions:
    print(f"The number {user_input} was found at positions: {positions}")
else:
    print(f"The number {user_input} was not found in the list.")
