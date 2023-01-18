#!/usr/bin/python3
"""
Module task1 about how to export data in the CSV format
"""

from sys import argv
from requests import get
from csv import writer

url_base = 'https://jsonplaceholder.typicode.com/users/'
file_name = f'{argv[1]}.csv'


def export_csv():
    """"""
    usr = get(url_base + argv[1]).json()
    tasks = get(url_base + argv[1] + '/todos').json()

    for task in tasks:
        data = [usr['id'], usr['username'], task['completed'], task['title']]
        with open(file_name, 'a', encoding='utf-8') as csvfile:
            csvwrite = writer(csvfile)
            csvwrite.writerow(data)


if __name__ == '__main__':
    export_csv()
