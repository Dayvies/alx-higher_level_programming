#!/usr/bin/python3
def safe_print_division(a, b):
    count = None
    try:
        count = a / b
    except BaseException:
        return count
    finally:
        print("Inside result: {}".format(count))
    return count
