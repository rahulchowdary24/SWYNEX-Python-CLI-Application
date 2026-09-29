"""Command-line interface for the task manager."""

from .core import TaskManager
from .storage import TaskStorage
from .validators import (
    validate_description,
    validate_status,
    validate_task_id,
    validate_title,
)

MENU = """
========================================
       SWYNEX TASK MANAGER
========================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
========================================
"""


def display_tasks(manager: TaskManager) -> None:
    tasks = manager.list_tasks()

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nID | Status      | Title")
    print("-" * 45)
    for task in tasks:
        print(f"{task.task_id:<2} | {task.status:<11} | {task.title}")
        if task.description:
            print(f"   Description: {task.description}")


def add_task(manager: TaskManager, storage: TaskStorage) -> None:
    try:
        title = validate_title(input("Enter task title: "))
        description = validate_description(input("Enter description: "))
        task = manager.add_task(title, description)
        storage.save(manager.tasks)
        print(f"\nTask #{task.task_id} added successfully.")
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}")


def update_task(manager: TaskManager, storage: TaskStorage) -> None:
    try:
        task_id = validate_task_id(input("Enter task ID to update: "))
        task = manager.find_task(task_id)

        print(f"Current title: {task.title}")
        title_input = input("New title (press Enter to keep current): ").strip()
        description_input = input(
            "New description (press Enter to keep current): "
        ).strip()
        status_input = input(
            "New status [Pending/In Progress/Completed] "
            "(press Enter to keep current): "
        ).strip()

        title = validate_title(title_input) if title_input else None
        description = validate_description(description_input) if description_input else None
        status = validate_status(status_input) if status_input else None

        manager.update_task(task_id, title, description, status)
        storage.save(manager.tasks)
        print("\nTask updated successfully.")
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}")


def delete_task(manager: TaskManager, storage: TaskStorage) -> None:
    try:
        task_id = validate_task_id(input("Enter task ID to delete: "))
        deleted = manager.delete_task(task_id)
        storage.save(manager.tasks)
        print(f"\nTask #{deleted.task_id} deleted successfully.")
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}")


def run() -> None:
    storage = TaskStorage()
    try:
        manager = TaskManager(storage.load())
    except (ValueError, OSError) as exc:
        print(f"Warning: {exc}")
        manager = TaskManager()

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                add_task(manager, storage)
            elif choice == "2":
                display_tasks(manager)
            elif choice == "3":
                update_task(manager, storage)
            elif choice == "4":
                delete_task(manager, storage)
            elif choice == "5":
                print("\nThank you for using SWYNEX Task Manager!")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 5.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except EOFError:
            print("\nInput ended. Goodbye!")
            break
