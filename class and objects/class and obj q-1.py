class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)


# Example usage
c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

print("First Complex Number:", c1)
print("Second Complex Number:", c2)

print("Addition:", c1.add(c2))
print("Subtraction:", c1.subtract(c2))
print("Multiplication:", c1.multiply(c2))
print("Division:", c1.divide(c2))
