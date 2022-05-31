#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    count = 0
    for c in str:
        if count == n:
            count += 1
            continue
        else:
            count += 1
            str2 += c
    return (str2)
