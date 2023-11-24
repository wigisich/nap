import os
from datetime import datetime, timedelta

class TodoItem:
    def __init__(
            self,
            task: str,
            deadline: tuple[int]|None = None, # (day, month, year)
            days: float|None = None,
            hours: float|None = None,
            ):
        self.deadline = datetime(*deadline[::-1]) if deadline else datetime.now()
        self.deadline = self.deadline + timedelta(days=days) if days else self.deadline
        self.deadline= self.deadline + timedelta(hours=hours) if hours else self.deadline
        self.task = task
        self.subtasks = []
        self.status = False
    def __repr__(self):
        return f"Deadline: {datetime.strftime(self.deadline, '%d/%m/%Y %H:%M')}\nTask: {self.task}"
