#!/usr/bin/python3
"""headers using requests"""
import requests
import sys


def main():
    """main function"""
    try:
        q = sys.argv[1]
    except Exception:
        q = ""
    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        z = response.json()
        if z == {}:
            print("No result")
        else:
            print("[{}] {}".format(z.get('id'), z.get('name')))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
