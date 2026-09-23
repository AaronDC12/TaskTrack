"""A command-line task manager created for CPS 310.

Author: Aaron Dcunha
Course: CPS 310
"""

TASKS_FILE = "tasks.txt"


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ").strip()

    if not task:
        print("A task cannot be empty.")
        return

    tasks.append(task)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def save_tasks(tasks, filename):
    """Save all tasks to a text file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                if not task:
                    continue
                tasks.append(task)
    except FileNotFoundError:
        return []

    return tasks


def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()