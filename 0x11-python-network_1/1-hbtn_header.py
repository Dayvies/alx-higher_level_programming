#!/usr/bin/python3
"""status urllib get header"""
import urllib.request
import sys


def main():
    """main function"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        x = dict(response.headers)
        print(x.get('X-Request-Id'))


if __name__ == "__main__":
    main()
