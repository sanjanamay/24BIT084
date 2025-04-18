def count_vowels(s):
    if not s:
        return 0
    return (1 if s[0].lower() in 'aeiou' else 0) + count_vowels(s[1:])

def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

def sanitize_list(lst):
    if not lst:
        return []
    return [0 if lst[0] < 0 else lst[0]] + sanitize_list(lst[1:])

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed list:", reverse_list(numbers))
print("Sanitized list:", sanitize_list(numbers))

a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))
print(f"{a}^{b} =", power(a, b))
