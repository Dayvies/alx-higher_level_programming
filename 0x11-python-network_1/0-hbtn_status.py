#!/usr/bin/python3
"""status urllib"""
import urllib.request


def main():
    """main function"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status'
                                ) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))


if __name__ == "__main__":
    main()
