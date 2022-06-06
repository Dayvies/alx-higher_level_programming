#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        ln = len(row)
        for n in range(ln):
            if n == ln - 1:
                print("{:d}".format(row[n]))
                continue
            else:
                print("{:d}".format(row[n]), end=' ')
