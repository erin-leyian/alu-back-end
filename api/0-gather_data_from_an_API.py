#!/usr/bin/python3
"""Fetch and display TODO list progress for a given employee."""

import requests
import sys


def main():
    """Main function to fetch tasks and display progress."""
    if len(sys.argv) < 2:
        return

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        return

    user_url = (
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    todo_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    )

    # Get user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return

    user_name = user_response.json().get('name')

    # Get todos
    todos = requests.get(todo_url).json()

    total_tasks = len(todos)
    completed_tasks = [task['title'] for task in todos
                       if task.get('completed')]

    # Print formatted result
    print(
        f"Employee {user_name} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    main()
