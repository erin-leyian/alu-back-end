#!/usr/bin/env python3

import requests
import sys

def fetch_todo_progress(employee_id):
    try:
        # Fetch employee details 
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

        user = requests.get(user_url).json()
        todos = requests.get(todo_url).json()

        if not user:
            print("Employee not found.")
            return

        employee_name = user.get("name")
        total_tasks = len(todos)
        done_tasks = [task for task in todos if task.get("completed")]
        number_of_done_tasks = len(done_tasks)

        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])
            fetch_todo_progress(emp_id)
        except ValueError:
            print("Employee ID must be an integer.")
       
           
         
         