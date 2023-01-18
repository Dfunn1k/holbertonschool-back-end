#!/usr/bin/python3
"""
Module for task0 about request and API
"""

import requests
from sys import argv

url_base = 'https://jsonplaceholder.typicode.com/users/'


def get_data():
    """ This function get data of the placeholders API"""
    name = requests.get(url_base + argv[1]).json()
    todos = requests.get(url_base + argv[1] + '/todos/').json()
    count = 0
    title = ""

    for item in todos:
        if item['completed'] is True:
            title += "\t {}\n".format(item['title'])
            count += 1

    output = f"Employee {name['name']} is done with tasks({count}/20):"
    print(output + f"\n{title}", end='')


if __name__ == '__main__':
    get_data()
