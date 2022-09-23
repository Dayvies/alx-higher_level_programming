#!/usr/bin/python3
"""headers using requests"""
import requests
import sys


def main():
    """main function"""
    response = requests.get(sys.argv[1])
    code = str(response.status_code)
    if code[0] == '4' or code[0] == '5':
        print("Error code: {}".format(code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
