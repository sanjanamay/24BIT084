people = ["Alice", ("John",), "Emma", ("Mike",), "Sophia", ("David",)]
num_boys = 0
num_girls = 0

for person in people:
    if isinstance(person, tuple):
        num_boys += 1
    else:
        num_girls += 1

print("Number of boys:", num_boys)
print("Number of girls:", num_girls)
