#!/usr/bin/python3
def calc2():
    import sys
    from calculator_1 import add, sub, mul, div
    lenl = len(sys.argv)
    if lenl != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opx = sys.argv[2]
    if opx == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif opx == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif opx == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif opx == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    calc2()
