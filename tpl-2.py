students = [
    (101, "Alice", 20),
    (102, "Bob", 21),
    (103, "Charlie", 19),
    (104, "Diana", 22)
]
roll_nos = []
names = []
ages = []
for student in students:
    roll_no, name, age = student
    roll_nos.append(roll_no)
    names.append(name)
    ages.append(age)

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
