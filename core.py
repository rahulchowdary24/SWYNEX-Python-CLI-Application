"""Core task-management operations."""

from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Task:
    task_id: int
    title: str
    description: str = ""
    status: str = "Pending"

    def to_dict(self):
        return asdict(self)


class TaskManager:
    """Business logic for creating, viewing, updating and deleting tasks."""

    def __init__(self, tasks: Optional[List[Task]] = None):
        self.tasks = tasks or []

    def next_id(self) -> int:
        return max((task.task_id for task in self.tasks), default=0) + 1

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(self.next_id(), title, description)
        self.tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def find_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} was not found.")

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Task:
        task = self.find_task(task_id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
        return task

    def delete_task(self, task_id: int) -> Task:
        task = self.find_task(task_id)
        self.tasks.remove(task)
        return task
