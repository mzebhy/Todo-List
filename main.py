
def show_menu():
    print("\n===== TODO LIST =====")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Delete a task")
    print("4. Mark task as completed")
    print("5. Exit")


def main():
    print("Welcome to Todo List App!")

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye!")
            break
        else:
            print("This feature will be added soon.")


if __name__ == "__main__":
    main()
