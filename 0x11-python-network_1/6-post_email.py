#!/usr/bin/python3
"""headers using requests"""
import requests
import sys


def main():
    """main function"""
    payload = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)


if __name__ == "__main__":
    main()
