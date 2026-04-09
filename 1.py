tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(i+1, task)

    elif choice == '3':
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted!")

    elif choice == '4':
        break

    else:
        print("Invalid choice")