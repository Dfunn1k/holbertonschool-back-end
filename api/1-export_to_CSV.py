#!/usr/bin/python3
"""
Module task1 about how to export data in the CSV format
"""

from sys import argv
from requests import get

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_csv():
    """"""
    usr = get(url_base + argv[1]).json()
    tasks = get(url_base + argv[1] + '/todos').json()
    file_name = argv[1] + '.csv'

    for task in tasks:
        data = '"' + str(usr['id']) + '",' + '"' + usr['username'] + '",' +\
               '"' + str(task['completed']) + '",' + '"' + task['title'] +\
               '"\n'

        with open(file_name, 'a', encoding='utf-8') as csvfile:
            csvfile.write(data)


if __name__ == '__main__':
    export_csv()
