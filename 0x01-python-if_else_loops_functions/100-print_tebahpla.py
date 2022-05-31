#!/usr/bin/python3
for char in range(122, 96, -1):
    print("{x}".format(x=chr(char) if char %
          2 == 0 else chr(char - 32)), end='')
