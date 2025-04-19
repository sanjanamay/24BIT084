def to_lower_case(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  
        else:
            result += char
    return result

def to_upper_case(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  
        else:
            result += char
    return result

def toggle_case(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  
        else:
            result += char
    return result
string = input("Enter a string: ")
print("Lowercase:", to_lower_case(string))
print("Uppercase:", to_upper_case(string))
print("Toggle case:", toggle_case(string))
