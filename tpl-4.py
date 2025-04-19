menu = [
    ("Burger", 120),
    ("Pizza", 250),
    ("Pasta", 180),
    ("Sandwich", 90),
    ("Fries", 70)
]

sorted_menu = sorted(menu, key=lambda item: item[1], reverse=True)

print("Menu sorted by price (high to low):")
for food, price in sorted_menu:
    print(f"{food}: ₹{price}")
