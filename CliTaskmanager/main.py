import argparse
import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_tasks(tasks: list[dict]) -> None:
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(title: str) -> None:
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: '{title}'")


def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{idx}. [{status}] {task['title']}")


def complete_task(index: int) -> None:
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Completed: '{tasks[index - 1]['title']}'")
    else:
        print("Invalid task number.")


def delete_task(index: int) -> None:
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: '{removed['title']}'")
    else:
        print("Invalid task number.")


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI task manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("title", help="Title of the task")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task completed")
    done_parser.add_argument("index", type=int, help="Task number to complete")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task number to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)


if __name__ == "__main__":
    main()
