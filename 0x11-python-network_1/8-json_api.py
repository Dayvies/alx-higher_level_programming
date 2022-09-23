#!/usr/bin/python3
"""headers using requests"""
import requests
import sys
import json


def main():
    """main function"""
    try:
        q = sys.argv[1]
    except Exception:
        q = ""
    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    str_js = response.text
    try:
        z = json.loads(str_js)
        if z == {}:
            print("No result")
        else:
            print("[{}] {}".format(z['id'], z['name']))
    except Exception:
        print("Not a alid JSON")


if __name__ == "__main__":
    main()
