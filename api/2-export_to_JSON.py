#!/usr/bin/python3
"""
Module documentation for task 2 about retrieve json
"""

from sys import argv
from json import dumps
from requests import get

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_json():
    """function that retrieve data in format json"""

    file_name = argv[1] + '.json'
    todos = get(url_base + argv[1] + '/todos/').json()
    items_data = []
    retrieve_json = dict()

    for todo in todos:
        del todo['userId']
        items_data.append(todo)

    retrieve_json[argv[1]] = items_data

    with open(file_name, 'w', encoding='utf-8') as file_json:
        file_json.write(dumps(retrieve_json))


if __name__ == '__main__':
    export_json()