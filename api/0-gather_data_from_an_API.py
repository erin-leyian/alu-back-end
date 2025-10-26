#!/usr/bin/python3
"""
Script that uses a REST API for a given employee ID
and returns the TODO list progress.
"""

import requests
import sys


def main():
    if len(sys.argv) < 2:
        return

    user_id = sys.argv[1]

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return

    user_name = user_response.json().get('name')

    # Get todos
    todos = requests.get(todos_url).json()
    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]
    total_tasks = len(todos)

    # EXACT formatting
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()