#!/usr/bin/python3
def remove_char_at(str, n):
    c = 0
    new = ""
    for i in str:
        if c != n:
            new += i
        c += 1
    return new
