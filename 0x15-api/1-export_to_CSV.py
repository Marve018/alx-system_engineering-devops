#!/usr/thon3
"""Gathring data from an API """

from requests import get
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    # retrive the employee data info
    response = get(url + "users/{}".format(sys.argv[1]))
    employee = response.json().get("usermame")

    # retrive todo list
    response = get(url + "users/{}/todos".format(sys.argv[1]))
    todos = response.json()

    with open('{}.csv'.format(sys.argv[1]), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(sys.argv[1], employee,
                               todo.get('completed'),
                               todo.get('title')))
