def assign_grade(marks):
    if marks == "Absent":
        return "NA"
    elif marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    elif marks <= 79:
        return "A+"
    elif marks <= 100:
        return "O"
marks1 = input("Enter marks for subject 1 (or type 'Absent' if absent): ")
marks2 = input("Enter marks for subject 2 (or type 'Absent' if absent): ")
marks3 = input("Enter marks for subject 3 (or type 'Absent' if absent): ")

if marks1 != "Absent":
    marks1 = int(marks1)
if marks2 != "Absent":
    marks2 = int(marks2)
if marks3 != "Absent":
    marks3 = int(marks3)

if (marks1 != "Absent" and marks1 <= 39) or (marks2 != "Absent" and marks2 <= 39) or (marks3 != "Absent" and marks3 <= 39):
    result = "Fail"
else:
    result = "Pass"

# Calculate total and average
total = 0
subjects = [marks1, marks2, marks3]
for mark in subjects:
    if mark != "Absent":
        total += mark
average = total / len([mark for mark in subjects if mark != "Absent"])

print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Result: {result}")
print(f"Grades: {[assign_grade(mark) for mark in subjects]}")
