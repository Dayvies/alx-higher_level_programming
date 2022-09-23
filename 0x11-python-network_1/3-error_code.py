#!/usr/bin/python3
"""status urllib get header"""
import urllib.error
import urllib.request
import sys


def main():
    """main function"""

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
