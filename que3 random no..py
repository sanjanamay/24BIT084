import random

random_numbers = random.sample(range(-15,16),10)

squared_numbers = [x ** 2 for x in random_numbers]

print(random_numbers)
print(squared_numbers)
