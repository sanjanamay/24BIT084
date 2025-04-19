# Function to convert to lower case
def to_lower_case(input_string):
    result = ''
    for char in input_string:
        if 'A' <= char <= 'Z':  # Check if char is uppercase
            result += chr(ord(char) + 32)  # Convert to lowercase by adding 32
        else:
            result += char
    return result

# Function to convert to upper case
def to_upper_case(input_string):
    result = ''
    for char in input_string:
        if 'a' <= char <= 'z':  # Check if char is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase by subtracting 32
        else:
            result += char
    return result

# Function to toggle case
def toggle_case(input_string):
    result = ''
    for char in input_string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  # Convert to uppercase
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char
    return result


input_string = input("Enter a string: ")
print("Lower case:", to_lower_case(input_string))
print("Upper case:", to_upper_case(input_string))
print("Toggled case:", toggle_case(input_string))
