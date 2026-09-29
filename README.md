# SWYNEX Python CLI Application

A beginner-friendly **Task Manager CLI application** built with Python for **SWYNEX Task 1**.

## Features

- Add tasks
- View all tasks
- Update task title, description and status
- Delete tasks
- Persistent storage using JSON
- Input validation
- Exception handling
- Modular Python structure
- Uses functions, classes and modules

## Project Structure

```text
SWYNEX-Python-CLI-Application/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── tasks.json
│
└── task_manager/
    ├── __init__.py
    ├── cli.py
    ├── core.py
    ├── storage.py
    └── validators.py
```

## Requirements

- Python 3.9 or newer
- No external libraries are required.

## How to Run

### 1. Open the project folder

```bash
cd SWYNEX-Python-CLI-Application
```

### 2. Run the application

```bash
python app.py
```

On some systems, use:

```bash
python3 app.py
```

## Example

```text
========================================
       SWYNEX TASK MANAGER
========================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
========================================
Choose an option (1-5): 1

Enter task title: Complete Python assignment
Enter description: Finish SWYNEX Task 1

Task #1 added successfully.
```

## Validation and Exception Handling

The project validates:

- Empty task titles
- Maximum title length
- Maximum description length
- Numeric and positive task IDs
- Valid task statuses
- Invalid menu choices
- JSON file errors
- File access errors
- Keyboard interruption and end-of-input

## Learning Outcomes

This project demonstrates:

1. Python functions
2. Classes and objects
3. Modules and packages
4. File handling
5. JSON data storage
6. Input validation
7. Exception handling
8. Command-line interfaces
9. Basic software project structure
10. Git and GitHub workflow

## GitHub Repository Name

Recommended:

`SWYNEX-Python-CLI-Application`

## Author

Student project created for SWYNEX Task 1.
