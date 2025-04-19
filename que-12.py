import math
cx, cy = map(float, input("Enter center (x, y): ").split())
r = float(input("Enter radius: "))
px, py = map(float, input("Enter point (x, y): ").split())

distance = math.sqrt(pow(px - cx, 2) + pow(py - cy, 2))
print("Inside" if distance < r else "On" if distance == r else "Outside")
