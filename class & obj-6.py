class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

    def display(self):
        return f"{self.date[0]:02}/{self.date[1]:02}/{self.date[2]}"

date1 = Date(23, 4, 2025)
date2 = Date(23, 4, 2025)
date3 = Date(1, 1, 2023)

print("Date 1:", date1.display())
print("Date 2:", date2.display())
print("Date 3:", date3.display())

print("Date 1 == Date 2:", date1 == date2)  
print("Date 1 == Date 3:", date1 == date3)  
