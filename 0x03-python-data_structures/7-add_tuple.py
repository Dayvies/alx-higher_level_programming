#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    x = len(tuple_a)
    z = len(tuple_b)
    if x > 2:
        x = 2
    if z > 2:
        z = 2
    for n in range(x):
        a[n] = tuple_a[n]
    for n in range(z):
        b[n] = tuple_b[n]
    return (a[0] + b[0], b[1] + a[1])
