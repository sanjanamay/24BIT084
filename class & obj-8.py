class MyString:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        self.text += other.text
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def display(self):
        print(self.text)

s1 = MyString("Hello")
s2 = MyString("World")

print("Original Strings:")
s1.display()
s2.display()

s1 += s2
print("\nAfter Concatenation:")
s1.display()

s1.toLower()
print("\nAfter toLower():")
s1.display()

s1.toUpper()
print("\nAfter toUpper():")
s1.display()
