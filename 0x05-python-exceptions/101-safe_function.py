#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    x = None
    try:
        x = fct(*args)
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
    return x
