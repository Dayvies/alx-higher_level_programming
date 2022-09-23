#!/usr/bin/python3
"""headers using requests"""
import requests
import sys


def main():
    """main function"""

    user = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    login = requests.get(user)
    x = login.json()
    count = 0
    for instance in x:
        if count == 10:
            return
        commit = instance.get('commit')
        commiter = commit.get('author').get('name')
        sha = instance.get('sha')
        print('{}: {}'.format(sha, commiter))
        count += 1


if __name__ == "__main__":
    main()
