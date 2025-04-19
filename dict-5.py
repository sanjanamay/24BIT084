grocery_prices = {
    "apple": 30,
    "banana": 20,
    "carrot": 10,
    "milk": 50,
    "bread": 25
}
grocery_quantities = {
    "apple": 2,
    "banana": 5,
    "carrot": 3,
    "milk": 1,
    "bread": 2
}
total_bill = 0
for item in grocery_prices:
    if item in grocery_quantities:  # Check if the item exists in the quantities dictionary
        total_bill += grocery_prices[item] * grocery_quantities[item]
print(f"Total Bill: ₹{total_bill}")
