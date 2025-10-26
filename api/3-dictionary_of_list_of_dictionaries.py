#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    # Create dictionary of list of dictionaries
    all_tasks = {
        user.get("id"): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            }
            for task in requests.get(url + "todos",
                                     params={"userId": user.get("id")}).json()
        ]
        for user in users
    }

    # Export to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)