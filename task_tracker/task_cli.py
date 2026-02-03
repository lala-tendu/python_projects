import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# ---------- Utility Functions ----------

def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------- Task Operations ----------

def add_task(description):
    tasks = load_tasks()

    task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": current_time(),
        "updatedAt": current_time()
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")


def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = current_time()
            save_tasks(tasks)
            print("Task updated successfully")
            return

    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(new_tasks):
        print("Task not found")
        return

    save_tasks(new_tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = current_time()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return

    print("Task not found")


def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")


# ---------- CLI Handler ----------

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  task-cli add \"description\"")
        print("  task-cli update <id> \"description\"")
        print("  task-cli delete <id>")
        print("  task-cli mark-in-progress <id>")
        print("  task-cli mark-done <id>")
        print("  task-cli list [todo|in-progress|done]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            add_task(sys.argv[2])

        elif command == "update":
            update_task(int(sys.argv[2]), sys.argv[3])

        elif command == "delete":
            delete_task(int(sys.argv[2]))

        elif command == "mark-in-progress":
            mark_task(int(sys.argv[2]), "in-progress")

        elif command == "mark-done":
            mark_task(int(sys.argv[2]), "done")

        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else None
            list_tasks(status)

        else:
            print("Unknown command")

    except IndexError:
        print("Invalid arguments. Use correct command format.")
    except ValueError:
        print("Task ID must be a number.")


# ---------- Entry Point ----------

if __name__ == "__main__":
    main()
