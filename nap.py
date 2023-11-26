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
        screen_x, screen_y = os.get_terminal_size()
        limit_y = int(screen_x*.6)
        limit_task = int(screen_x*.4)
        deadline = f"{datetime.strftime(self.deadline, '%d/%m/%Y %H:%M')}"
        cut = True if len(self.task)>limit_task else False
        task = self.task[: limit_task-3 if cut else None] + "..." if cut else self.task
        task = "[ " + task.center(limit_y, " ") + " ]"
        return task

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

naps = [TodoItem(task="Task to do"), TodoItem(task="Another very very long task to do and it is so long that I don't know what to do with this task which implies that I need a professional help from who knows how to do this task especially when you know nothing about how to do the task within a short time of period that is either lower than at least on hour or maybe two.")]

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







