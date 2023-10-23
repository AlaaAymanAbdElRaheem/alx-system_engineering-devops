#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    task_response = requests.get(url + "users/{}/todos".format(user_id))
    tasks = task_response.json()
    completed_tasks = 0
    for task in tasks:
        if task["completed"] is True:
            completed_tasks += 1
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    user_name = user["name"]
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          completed_tasks,
                                                          len(tasks)))
    for task in tasks:
        if task["completed"] is True:
            print("\t {}".format(task["title"]))
