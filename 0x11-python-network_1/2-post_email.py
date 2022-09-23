#!/usr/bin/python3
"""status urllib get header"""
import urllib.parse
import urllib.request
import sys


def main():
    """main function"""
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))


if __name__ == "__main__":
    main()
