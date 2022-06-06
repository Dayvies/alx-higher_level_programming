#!/usr/bin/python3
def max_integer(my_list=[]):
    z = len(my_list)
    x = 0
    if (z <= 0):
        return None
    for n in range(z):
        if (n == 0):
            x = my_list[0]
        elif x < my_list[n]:
            x = my_list[n]
        else:
            continue
    return x
