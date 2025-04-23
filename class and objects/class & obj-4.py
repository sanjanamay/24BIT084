import math

class Shape:
    def __init__(self):
        self.shape_type = ""
        self.size = 0

    def accept_data(self):
        self.shape_type = input("Enter shape (circle/square/triangle): ").lower()
        if self.shape_type == "circle":
            self.size = float(input("Enter radius: "))
        elif self.shape_type == "square":
            self.size = float(input("Enter side length: "))
        elif self.shape_type == "triangle":
            self.size = float(input("Enter side length of equilateral triangle: "))
        else:
            print("Unsupported shape.")

    def area(self):
        if self.shape_type == "circle":
            return math.pi * self.size ** 2
        elif self.shape_type == "square":
            return self.size ** 2
        elif self.shape_type == "triangle":
            return (math.sqrt(3) / 4) * self.size ** 2
        else:
            return None

    def perimeter(self):
        if self.shape_type == "circle":
            return 2 * math.pi * self.size
        elif self.shape_type == "square":
            return 4 * self.size
        elif self.shape_type == "triangle":
            return 3 * self.size
        else:
            return None
s = Shape()
s.accept_data()

print("Area:", s.area())
print("Perimeter/Circumference:", s.perimeter())
