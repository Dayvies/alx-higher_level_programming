#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    z = len(my_list)
    if z > 1:
        my_list.reverse()
    for i in my_list:
        print("{}".format(i))