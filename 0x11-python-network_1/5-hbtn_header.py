#!/usr/bin/python3
"""headers using requests"""
import requests


def main():
    """main function"""
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(response.headers['X-Request-Id'])


if __name__ == "__main__":
    main()
