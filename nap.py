import os
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(
            description = "Example description",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        )

parser.add_argument("-at", "--add-task", help="add a task")
parser.add_argument("-ast", "--add-subtask", action="append", help="add a subtask")

parser.add_argument("-end", "--deadline", help="set the deadline")
parser.add_argument("-day", "--days", help="set deadline as n-days later")
parser.add_argument("-hr", "--hours", help="set deadline as n-hours later")

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
print(config)

class Nap:
    def __init__(self, **kwargs):
        self.deadline = datetime.strptime(kwargs["deadline"], "%d-%m-%Y") if kwargs["deadline"] else datetime.now()
        self.deadline = self.deadline + timedelta(days=float(kwargs["days"])) if kwargs["days"] else self.deadline
        self.deadline = self.deadline + timedelta(hours=float(kwargs["hours"])) if kwargs["hours"] else self.deadline
        self.task =  kwargs["add_task"]
        self.subtasks = kwargs["add_subtask"]
        self.status = True
    def __repr__(self):
        limit = 12
        task = self.task[:limit if len(self.task)>limit else None] + "..." if len(self.task)>limit else self.task
        return f"<Task: {task}, Deadline: {datetime.strftime(self.deadline, '%d/%m/%Y %H:%M')}, Subtasks: {len(self.subtasks)}>"

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def display(self, idx, subtasks=False):
        x, y = os.get_terminal_size()
        limit_task = int(x*.4)
        limit_x = int(x*.6)
        cut = True if len(self.task)>limit_task else False
        task = self.task[:limit_task if cut else None]+"..." if cut else self.task
        task = f"  [{self.deadline.strftime('%d-%m-%Y')}] - [ {task} ({idx})]\n"
        if subtasks:
            for i, subtask in enumerate(self.subtasks):
                cut = True if len(subtask)>limit_task else False
                subtask = subtask[:limit_task-4 if cut else None]+"..." if cut else subtask
                subtask = f"  \t\t - [ {subtask} ({i})]\n"
                task = task + subtask
        return task

naps = [Nap(add_task="Some task", add_subtask=["subtask1", "subtask2"], deadline=None, hours=None, days=None), Nap(add_task="Some task", add_subtask=["subtask1", "subtask2"], deadline=None, hours=None, days=None)]

def display_naps(naps):
    print("\n__naps__:\n---------\n")
    for idx, n in enumerate(naps):
        if n.status: print(n.display(idx=idx, subtasks=True))

if __name__ == "__main__":
    if config["add_task"]:
        nap = Nap(**config)
        naps.append(nap)
    if config["check"]:
        idx = int(config["task"])
        naps[idx].status = not naps[idx].status
    display_naps(naps)



