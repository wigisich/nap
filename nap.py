from datetime import datetime, timedelta

class TodoItem:
    def __init__(
            self,
            task: str,
            deadline: tuple[int]|None = None, # (day, month, year)
            days: float|None = None,
            hours: float|None = None,
            ):
        now = datetime.now
        self.deadline = datetime(*deadline[::-1]) if deadline else None
        self.days = now().date() + timedelta(days=days) if days else None
        self.hours = now() + timedelta(hours=hours) if hours else None
        self.task = task
        self.subtasks = []
        self.status = False

