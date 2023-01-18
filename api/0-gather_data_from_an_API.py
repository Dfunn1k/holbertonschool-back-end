#!/usr/bin/python3
""" Module for task0 """


if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/'
    name = requests.get(url + argv[1]).json()
    todos = requests.get(url + argv[1] + '/todos/').json()
    count = 0
    title = ""

    for item in todos:
        if item['completed'] is True:
            title += "\t {}\n".format(item['title'])
            count += 1

    output_1 = f"Employee {name['name']} is done with tasks({count}/20):"
    output_2 = output_1 + f"\n{title}"
    print(output_2, end='')
