stack = []

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(f"{element} pushed onto stack.")

def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
    else:
        popped = stack.pop()
        print(f"{popped} popped from stack.")

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents (top to bottom):")
        for item in reversed(stack):
            print(item)

while True:
    print("\n=== Stack Menu ===")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
