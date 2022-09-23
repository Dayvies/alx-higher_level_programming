#!/usr/bin/python3
"""headers using requests"""
import requests
import sys


def main():
    """main function"""
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
