#!/usr/bin/python3
def infiadd():
    import sys
    sum = 0
    lenn = len(sys.argv)
    for n in range(1, lenn):
        sum += int(sys.argv[n])
    print("{:d}".format(sum))


if __name__ == "__main__":
    infiadd()
