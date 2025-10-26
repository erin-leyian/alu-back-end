#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys


def main():
    """main function"""
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <user_id>")
        return

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("User ID must be an integer")
        return

    # API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    # Get user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        return

    user_name = user_response.json().get('name')

    # Get todo list for this user only
    todos = requests.get(todo_url).json()

    # Count tasks
    total_tasks = len(todos)
    completed_tasks = [t['title'] for t in todos if t['completed']]

    # Output format
    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == '__main__':
    main()
