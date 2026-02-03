📝 Task Tracker CLI

A simple command-line task tracker built using Python that helps you manage tasks by tracking what you need to do, what’s in progress, and what’s completed.

This project is designed to practice:

Command-line interfaces (CLI)

File handling using JSON

Working with user input

Writing clean, modular Python code

🚀 Features

Add, update, and delete tasks

Mark tasks as todo, in-progress, or done

List all tasks

Filter tasks by status

Persistent storage using a JSON file

No external libraries required

🛠 Tech Stack

Language: Python 3

Storage: JSON file

Libraries: Python standard library only

📂 Project Structure
task-tracker/
├── task_cli.py      # Main CLI application
├── tasks.json       # Task storage (auto-created)
└── README.md

⚙️ Setup Instructions
1️⃣ Prerequisites

Make sure Python is installed:

python --version


Python 3.7+ is recommended.

2️⃣ Clone or Download the Project
git clone <repository-url>
cd task-tracker


Or download and extract the ZIP file.

▶️ How to Use

All commands are executed from the terminal using:

python task_cli.py <command> [arguments]

➕ Add a Task
python task_cli.py add "Learn Python"


Output:

Task added successfully (ID: 1)

✏️ Update a Task
python task_cli.py update 1 "Learn Python CLI"

🗑 Delete a Task
python task_cli.py delete 1

🔄 Mark Task Status

Mark task as in progress:

python task_cli.py mark-in-progress 1


Mark task as done:

python task_cli.py mark-done 1

📋 List Tasks

List all tasks:

python task_cli.py list


List completed tasks:

python task_cli.py list done


List pending tasks:

python task_cli.py list todo


List tasks in progress:

python task_cli.py list in-progress

🧾 Task Data Format

Tasks are stored in a JSON file with the following structure:

{
  "id": 1,
  "description": "Learn Python",
  "status": "todo",
  "createdAt": "2026-02-03 18:30:00",
  "updatedAt": "2026-02-03 18:30:00"
}

⚠️ Error Handling

Handles invalid commands gracefully

Prevents crashes due to missing arguments

Validates task IDs

Displays helpful usage messages

🧠 Learning Outcomes

Through this project, you will understand:

How CLI tools process user input

How to persist data without a database

How to safely read and write files

How real-world command-line utilities are structured

🌱 Future Improvements

Convert script into a global executable (task-cli)

Add sorting by creation date

Add search functionality

Add unit tests

Implement argparse for advanced CLI parsing

📜 License

This project is open-source and free to use for learning and personal projects.

🙌 Acknowledgements

Built as a learning project to strengthen Python fundamentals and system-level thinking.

✅ Tip for interviews

“This project demonstrates my understanding of CLI design, file-based persistence, and clean Python architecture without external dependencies.”