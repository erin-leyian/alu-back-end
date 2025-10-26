#!/usr/bin/python3
"""
Python script that returns information about TODO list progress
for a given employee ID using JSONPlaceholder API.
"""

import requests
import sys


def main():
    """Main function"""
    if len(sys.argv) < 2:
        return

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        return

    # Build URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Request user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return

    user_name = user_response.json().get("name")

    # Request todos for this user only
    todos = requests.get(todos_url).json()

    # Count total and completed
    total_tasks = len(todos)
    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]

    # Print EXACT format
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()
