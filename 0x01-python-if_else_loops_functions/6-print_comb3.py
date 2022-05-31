#!/usr/bin/python3
for n in range(0, 10):
    for j in range(n, 10):
        if n == j:
            continue
        if n == 8 and j == 9:
            print("{:d}{:d}".format(n, j))
            break
        print("{:d}{:d}".format(n, j), end=", ")
