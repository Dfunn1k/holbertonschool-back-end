#!/usr/bin/python3
"""
Module documentation for task 2 about retrieve json
"""

from sys import argv
from json import dump
from requests import get

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_json(id):
    """ function that retrieve data in format json """

    file_name = str(id) + '.json'
    usr = get(url_base + str(id)).json()
    todos = get(url_base + str(id) + '/todos/').json()
    items_data = []
    retrieve_json = dict()

    for todo in todos:
        item_dict = dict()
        item_dict['task'] = todo['title']
        item_dict['completed'] = todo['completed']
        item_dict['username'] = usr['username']
        items_data.append(item_dict)

    retrieve_json[str(id)] = items_data

    with open(file_name, 'w', encoding='utf-8') as file_json:
        dump(retrieve_json, file_json)


if __name__ == '__main__':
    export_json(int(argv[1]))
