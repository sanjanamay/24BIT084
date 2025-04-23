x1, y1 = float(input("Enter x1, y1: ").split())
x2, y2 = float(input("Enter x2, y2: ").split())
x3, y3 = float(input("Enter x3, y3: ").split())
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points lie on the same straight line.")
else:
    print("The points do not lie on the same straight line.")
