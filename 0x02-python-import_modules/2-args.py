#!/usr/bin/python3
def printarg():
    import sys
    lx = len(sys.argv) - 1
    print("{:d} argument{a}".format(
        lx, a="s." if lx == 0 else ":" if lx == 1 else "s:"))
    for n in range(1, lx+1):
        print("{:d}: {}".format(n, sys.argv[n]))


if __name__ == "__main__":
    printarg()
