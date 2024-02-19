#!/usr/bin/python3
"""Gathering data from an API """

import requests
import sys


if __name__ == "__main__":
    # Rest Api url
    url = "https://jsonplaceholder.typicode.com/"

    # retrive the employee data info
    response = requests.get(url + "users/{}".format(sys.argv[1]))
    employee = response.json()

    # retrive todo list
    response = requests.get(url +
                            "todos", params={"userId": sys.argv[1]})
    todos = response.json()

    # using list comprehenssion to filter & store completed list
    completed_tasks = [todo.get("title") for todo in todos
                       if todo.get("completed") is True]

    # get employee name
    employee_name = employee.get("name")

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), len(todos)))

    # print the titles of completed tasks with indentation
    [print("\t {}".format(c)) for c in completed_tasks]
