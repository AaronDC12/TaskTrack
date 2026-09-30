"""A command-line task manager created for CPS 310.

Author: Aaron Dcunha
Course: CPS 310
"""

TASKS_FILE = "tasks.txt"


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

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

def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    while True:
        view_tasks(tasks)
        selection = input(
            "Enter the number of the task to remove, or 0 to return to menu: "
        ).strip()

        # Allow the user to return to the menu.
        if selection == "0":
            print("Returning to menu.")
            return False

        # Reject input that is not numeric.
        if not selection.isdigit():
            print("Please enter a valid task number.")
            continue

        task_number = int(selection)

        # Reject numbers outside the valid task range.
        if task_number < 1 or task_number > len(tasks):
            print("That task number does not exist.")
            continue

        # Remove the selected task.
        removed_task = tasks.pop(task_number - 1)

        # Display confirmation.
        print(f"Task removed successfully: {removed_task}")

        return True


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
            if remove_task(tasks):
                save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")
if __name__ == "__main__":
    main()