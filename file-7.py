import pickle
from datetime import datetime
class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary
    
    def __repr__(self):
        return f"Employee(empcode={self.empcode}, empname={self.empname}, date_of_joining={self.date_of_joining}, salary={self.salary})"
def serialize_employee(emp, filename):
    with open(filename, 'wb') as file:
        pickle.dump(emp, file)
    print(f"Employee data has been serialized to {filename}")

def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        emp = pickle.load(file)
    return emp



emp = Employee(
    empcode=101,
    empname="John Doe",
    date_of_joining=datetime(2020, 5, 20),  
    salary=50000
)

filename = 'employee.pkl'
serialize_employee(emp, filename)

deserialized_emp = deserialize_employee(filename)
print("Deserialized Employee Data:", deserialized_emp)
