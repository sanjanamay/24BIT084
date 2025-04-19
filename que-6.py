num = input("Enter a number: ")
if num.startswith('-'):
    num = num[1:]

print("Number of digits:", len(num))
