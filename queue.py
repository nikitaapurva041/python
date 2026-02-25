queue = []

while True:
    print("\n------ QUEUE OPERATIONS ------")
    print("1. Enqueue (Insert)")
    print("2. Dequeue (Delete)")
    print("3. Display Queue")
    print("4. Front Element")
    print("5. Rear Element")
    print("6. Queue Size")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if not choice.isdigit():
        print("Invalid input! Please enter a number between 1 and 7.")
        continue

    choice = int(choice)

    if choice == 1:
        item = input("Enter element to insert: ")

        if item.isdigit():
            queue.append(int(item))
            print("Inserted:", item)
        else:
            print("Invalid element. Enter numbers only.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty. Cannot delete.")
        else:
            removed = queue.pop(0)
            print("Deleted element:", removed)

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", queue[0])

    elif choice == 5:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Rear element:", queue[-1])

    elif choice == 6:
        print("Queue size:", len(queue))

    elif choice == 7:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Choose between 1 and 7.")
