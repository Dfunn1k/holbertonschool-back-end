#!/usr/bin/python3
""" Module for task0"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/'
    first_request = requests.get(url + argv[1])
    employee_name = first_request.json()
    second_requests = requests.get(url + argv[1] + '/todos/')
    count = 0
    task = second_requests.json()
    title = ""

    for item in task:
        if item['completed'] is True:
            if item != task[19]:
                title += "\t {}\n".format(item['title'])
            else:
                title += "\t {}".format(item['title'])
            count += 1

    print("""Employee {} is done with tasks({}/20):
    {}""".format(employee_name['name'], count, title), end='')
