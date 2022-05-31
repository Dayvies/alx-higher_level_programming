#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    star = -1 * ((number * -1) % 10)
elif number > 0:
    star = number % 10
else:
    star = 0
print(f"Last digit of {number:d} is {star:d}", end=" ")
if star > 5:
    print("and is greater than 5")
elif star == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
