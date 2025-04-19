length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("Area is greater than perimeter")
else:
    print("Area is not greater than perimeter")
