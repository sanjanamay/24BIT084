def binary_equivalent(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

num = int(input("Enter a positive integer: "))
print("Binary equivalent:", binary_equivalent(num))






