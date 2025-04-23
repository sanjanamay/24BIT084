import math

class Cylinder:
    def __init__(self):
        self.radius = 0
        self.height = 0

    def accept_data(self):
        self.radius = float(input("Enter radius of the cylinder: "))
        self.height = float(input("Enter height of the cylinder: "))

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

c = Cylinder()
c.accept_data()

print("Surface Area of Cylinder:", c.surface_area())
print("Volume of Cylinder:", c.volume())
