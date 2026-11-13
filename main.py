
tasks = []


def show_menu():
    print("\n===== TODO LIST =====")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Delete a task")
    print("4. Mark task as completed")
    print("5. Exit")


def add_task():
    task = input("Enter your task: ")

    if task.strip():
        tasks.append({
            "title": task,
            "completed": False
        })
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['title']} - {status}")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    print("Welcome to Todo List App!")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("This feature will be added soon.")


if __name__ == "__main__":
    main()
