#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        star = ((number * -1) % 10)
    elif number > 0:
        star = number % 10
    else:
        star = 0
    print("{:d}".format(star), end="")
    return star
