"""Input validation helpers."""

VALID_STATUSES = {"Pending", "In Progress", "Completed"}


def validate_title(title: str) -> str:
    title = title.strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    if len(title) > 100:
        raise ValueError("Title must be 100 characters or fewer.")
    return title


def validate_description(description: str) -> str:
    description = description.strip()
    if len(description) > 500:
        raise ValueError("Description must be 500 characters or fewer.")
    return description


def validate_task_id(value: str) -> int:
    try:
        task_id = int(value)
    except ValueError as exc:
        raise ValueError("Task ID must be a number.") from exc

    if task_id <= 0:
        raise ValueError("Task ID must be a positive number.")
    return task_id


def validate_status(status: str) -> str:
    status = status.strip().title()
    if status not in VALID_STATUSES:
        allowed = ", ".join(sorted(VALID_STATUSES))
        raise ValueError(f"Invalid status. Choose: {allowed}")
    return status
