#!/usr/bin/python3
for one in range(97, 123):
    if one == ord('e') or one == ord('q'):
        continue
    print("{}".format(chr(one)), end='')
