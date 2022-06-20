#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for n in my_list:
        try:
            if count == x:
                break
            print(n, end='')
            count += 1
        except BaseException as err:
            return count
    print()
    return count
