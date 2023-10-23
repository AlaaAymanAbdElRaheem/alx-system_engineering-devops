#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    task_response = requests.get(url + "users/{}/todos".format(user_id))
    tasks = task_response.json()
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    user_name = user["username"]
    file_name = "{}.csv".format(user_id)
    tasks_list = []

    for task in tasks:
        tasks_list.append({"task": task["title"],
                           "completed": task["completed"],
                           "username": user_name})
    json_dict = {user_id: tasks_list}

    file_name = "{}.json".format(user_id)
    with open(file_name, mode='w') as json_file:
        json.dump(json_dict, json_file)
