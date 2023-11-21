#!/bin/bash

NAP_FILE="$HOME/.nap"

# Function to display the todo list
display_todo() {
    echo "List of tasks:"
    if [ -e "$NAP_FILE" ]; then
        cat "$NAP_FILE" | nl
    else
        echo "No tasks found."
    fi
}

# Function to add a task
add_task() {
    echo "$1" >> "$NAP_FILE"
    echo "Task added: $1"
}

# Function to mark a task as done
mark_as_done() {
    if [ -e "$NAP_FILE" ]; then
        sed -i "${1}s/^/[x] /" "$NAP_FILE"
        echo "Marked task $1 as done."
    else
        echo "No tasks found."
    fi
}

# Check if the script is called with arguments
if [ "$#" -gt 0 ]; then
    case "$1" in
        "display")
            display_todo
            ;;
        "add")
            if [ "$#" -gt 1 ]; then
                add_task "${*:2}"
            else
                echo "Usage: $0 add <task>"
            fi
            ;;
        "done")
            if [ "$#" -gt 1 ]; then
                mark_as_done "$2"
            else
                echo "Usage: $0 done <task_number>"
            fi
            ;;
        *)
            echo "Invalid command. Usage: $0 [display | add <task> | done <task_number>]"
            ;;
    esac
else
    echo "Usage: $0 [display | add <task> | done <task_number>]"
fi

