#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for n in range(x):
        try:
            if count == x:
                break
            print("{:d}".format(my_list[n]), end='')
            count += 1
        except IndexError:
            raise
        except TypeError:
            continue
        except ValueError:
            continue

    print()
    return count
