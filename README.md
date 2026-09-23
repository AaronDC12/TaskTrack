# TaskTrack

TaskTrack is a command-line task manager created for CPS 310. It allows users to view tasks, add new tasks, and save task data so that tasks remain available when the program is run again.

## Current Features

- View the current list of tasks
- Add new tasks
- Reject empty task input
- Load tasks from `tasks.txt` when the program starts
- Save new tasks to `tasks.txt`
- Handle a missing task file without crashing
- Handle invalid menu choices

## Requirements

- Python 3
- Git and GitHub for version control

## Project Files

- `tasktrack.py` — Main Python program
- `tasks.txt` — Stores the task data
- `README.md` — Project documentation
- `.gitignore` — Specifies files Git should ignore

## How to Run

Open a terminal in the TaskTrack project folder and run:

```text
python tasktrack.py
```

Use the menu to view tasks, add a task, or exit the program.

## Persistent Task Storage

TaskTrack uses `tasks.txt` to store task data. When the program starts, it loads the existing tasks from the file. When a new task is added, it is saved to the file so that it remains available after the program is closed and started again.

## Sample Interaction

```text
1. View tasks
2. Add task
3. Exit
Choose an option: 1

Tasks:
1. Complete ICA04
2. Review GitHub commands
3. Update the TaskTrack README
4. Test persistent storage

1. View tasks
2. Add task
3. Exit
Choose an option: 2
Enter a new task: Finish README
Task added successfully.
```

## Limitations and Planned Improvements

TaskTrack currently uses a simple text file for storage and provides only basic task management features. Planned improvements could include allowing users to delete or edit tasks, marking tasks as complete, and providing more advanced task organization.
## Version Control

TaskTrack uses Git to keep track of changes to the project. A commit records a set of changes in the local Git repository with a message describing what was changed. A push sends local commits to the GitHub repository so the changes are stored remotely. A pull downloads and integrates changes from the GitHub repository into the local working copy. This workflow makes it possible to keep different copies of the project synchronized.
