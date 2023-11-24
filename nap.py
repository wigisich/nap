import os
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(
            description = "Example description",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        )

parser.add_argument("-a", "--add-task", help="add a task/subtask")
parser.add_argument("-d", "--deadline", help="set the deadline")
parser.add_argument("-t", "--task", help="select a task")
parser.add_argument("-st", "--subtask", help="select a subtask of a task")

parser.add_argument("-c", "--check", action="store_true", help="check a task")
parser.add_argument("-u", "--uncheck", action="store_true", help="uncheck a task")
parser.add_argument("-del", "--delete", action="store_true", help="delete a task")

parser.add_argument("-s", "--sort", action="store_true", help="sort by date")
parser.add_argument("-i", "--important", action="store_true", help="highlight & pick the task to the top")

parser.add_argument("-fn", "--fnaps", help="finished naps")



args = parser.parse_args()
config = vars(args)

class TodoItem:
    def __init__(
            self,
            task: str,
            deadline: tuple[int]|None = None, # dd-mm-yyyy
            days: float|None = None,
            hours: float|None = None,
            ):
        self.deadline = datetime.strptime(deadline, "%d-%m-%Y") if deadline else datetime.now()
        self.deadline = self.deadline + timedelta(days=days) if days else self.deadline
        self.deadline = self.deadline + timedelta(hours=hours) if hours else self.deadline
        self.task = task
        self.subtasks = []
        self.status = False
    def __repr__(self):
        return f"Deadline: {datetime.strftime(self.deadline, '%d/%m/%Y %H:%M')}\nTask: {self.task}"

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

naps = [TodoItem(task="Task to do"), TodoItem(task="Another task to do...")]

if __name__ == "__main__":
    if not config:
        nap_display()

#  __naps__:
#  ---------
#  [ Bir şeyler yapmamız gerekiyor... (24) ]   [ 24/11/2023 ]
#   - [ Alt işlerden biri (13) ]
#   - [ Alt işlerden diğeri (42) ]
#
#  __fnaps__:
#  ----------
#  [ sdgfsdfg sdgf sdfg sdfg (54) ]
#  [ gergegw wgfwertgw gwgwe (77) ]
#  ...
#







