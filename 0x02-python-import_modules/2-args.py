#!/usr/bin/python3
def printarg():
    import sys
    lenn = len(sys.argv) - 1
    print("{:d} argument{a}".format(lenn,
                                    a="s." if lenn == 0 else ":" if lenn == 1 else "s:"))
    for n in range(1, lenn+1):
        print("{:d}: {}".format(n, sys.argv[n]))


if __name__ == "__main__":
    printarg()
