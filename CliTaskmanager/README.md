# CLI Task Manager

A small command-line task manager written in Python. Tasks are stored locally in `tasks.json` in the directory where you run the program.

## Requirements

- requires python 3.9 or newer

## Usage

Run these commands from the project directory:

```bash
python3 main.py add "Buy groceries"
python3 main.py list
python3 main.py done 1
python3 main.py delete 1
```

Task numbers are shown by `list` and are used by `done` and `delete`.

## Commands

- `add <title>` — add a task
- `list` — show all tasks
- `done <number>` — mark a task complete
- `delete <number>` — delete a task
