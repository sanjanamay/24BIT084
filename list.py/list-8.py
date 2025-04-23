queue = []

def enqueue():
    element = input("Enter element to enqueue: ")
    queue.append(element)
    print(f"{element} added to the queue.")

def dequeue():
    if not queue:
        print("Queue is empty. Cannot dequeue.")
    else:
        removed = queue.pop(0)
        print(f"{removed} removed from the queue.")

def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue contents (front to rear):")
        for item in queue:
            print(item)
while True:
    print("\n=== Queue Menu ===")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
