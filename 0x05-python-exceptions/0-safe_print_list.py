#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if not my_list:
        return count
    for n in my_list:
        try:
            print(n, end='')
            count += 1
            if count == x:
                break
        except BaseException as err:
            return count
    print()
    return count
