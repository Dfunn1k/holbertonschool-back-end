#!/usr/bin/python3
"""
Module documentation for a retrieve data in JSON format
"""

from sys import argv
from requests import get
from json import dump

url_base = 'https://jsonplaceholder.typicode.com/users/'


def dict_of_the_dict():
    """s"""
    users = get(url_base).json()
    retrieve_json = dict()

    for user in users:
        usr_id = user['id']
        item_data = []
        task_users = get(url_base + str(usr_id) + '/todos/').json()

        for todo in task_users:
            item_dict = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': user['username']
            }
            item_data.append(item_dict)
        retrieve_json[usr_id] = item_data

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file_json:
        dump(retrieve_json, file_json)


if __name__ == '__main__':
    dict_of_the_dict()
