#!/usr/bin/python3
"""headers using requests"""
import requests
import sys
import json


def main():
    """main function"""
    authorization = f'token {sys.argv[2]}'
    headers = {
        "Authorization": authorization,
    }
    user = 'https://api.github.com/users/{}'.format(sys.argv[1])
    login = requests.get(user, headers=headers)
    x = json.loads(login.text)
    print(x.get('id'))


if __name__ == "__main__":
    main()
