#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_bool = []
    for x in my_list:
        if x % 2 == 0:
            my_bool.append(True)
        else:
            my_bool.append(False)
    return my_bool
