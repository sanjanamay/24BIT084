company_data = {
    101: [(1, 25000), (2, 30000), (3, 20000)],  
    102: [(4, 35000), (5, 40000), (6, 45000)],  
    103: [(7, 28000), (8, 32000), (9, 27000)],  
}
dept_salary = {}
for dept_no, employees in company_data.items():
    
    salaries = [salary for roll_no, salary in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)
    dept_salary[dept_no] = {'min_salary': min_salary, 'max_salary': max_salary}
print("Department-wise Minimum and Maximum Salaries:")
for dept_no, salary_info in dept_salary.items():
    print(f"Department {dept_no}: Min Salary = {salary_info['min_salary']}, Max Salary = {salary_info['max_salary']}")
