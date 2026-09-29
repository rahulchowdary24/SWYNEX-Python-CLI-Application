"""JSON file storage for tasks."""

import json
from pathlib import Path
from typing import List

from .core import Task


class TaskStorage:
    def __init__(self, file_path: str = "data/tasks.json"):
        self.file_path = Path(file_path)

    def load(self) -> List[Task]:
        try:
            if not self.file_path.exists():
                return []

            with self.file_path.open("r", encoding="utf-8") as file:
                raw_tasks = json.load(file)

            if not isinstance(raw_tasks, list):
                raise ValueError("Task data must be a JSON list.")

            return [Task(**item) for item in raw_tasks]

        except (json.JSONDecodeError, TypeError, KeyError, ValueError) as exc:
            raise ValueError(f"Could not read task data: {exc}") from exc
        except OSError as exc:
            raise OSError(f"Could not access storage file: {exc}") from exc

    def save(self, tasks: List[Task]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump([task.to_dict() for task in tasks], file, indent=4)
        except OSError as exc:
            raise OSError(f"Could not save task data: {exc}") from exc
