#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    task_response = requests.get(url + "users/{}/todos".format(user_id))
    tasks = task_response.json()
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    user_name = user["username"]
    file_name = "{}.csv".format(user_id)

    with open(file_name, mode='w') as csv_file:
        writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user_name,
                             task["completed"], task["title"]])
