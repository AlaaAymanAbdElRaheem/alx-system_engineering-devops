#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    user_tasks = {}

    for user in users:
        user_id = user.get("id")
        task_response = requests.get(url + "users/{}/todos".format(user_id))
        tasks = task_response.json()

        all_tasks = []
        for task in tasks:
            all_tasks.append({"username": user.get("username"),
                              "task": task.get("title"),
                              "completed": task.get("completed")})

        user_tasks[user_id] = all_tasks

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(user_tasks, json_file)
