import pandas as pd
filename = 'students_data.xlsx'  
df = pd.read_excel(filename)
students_dict = []
for index, row in df.iterrows():
    student = {
        'RollNo': row['RollNo'],
        'Name': row['Name'],
        'Marks_1': row['Marks_1'],
        'Marks_2': row['Marks_2'],
        'Marks_3': row['Marks_3'],
        'Total': row['Marks_1'] + row['Marks_2'] + row['Marks_3']
    }
    students_dict.append(student)
print(students_dict)
