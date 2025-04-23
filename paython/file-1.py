import csv
data = [
    ['Name', 'Age', 'Department'],
    ['John Doe', 30, 'Computer Science'],
    ['Alice Smith', 25, 'Mathematics'],
    ['Bob Brown', 40, 'Physics'],
    ['Sarah Clark', 28, 'Chemistry']
]
filename = 'faculty_data.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' has been created successfully.")
