#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for c in str:
        x = ord(c)
        if x >= 97 and x < 123:
            str2 += chr(x - 32)
            continue
        else:
            str2 += c
    print("{}".format(str2))
