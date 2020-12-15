#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    for i in range(0, 2):
        if not a[i]:
            a.append(0)
        if not b[i]:
            b.append(0)
    c = (a[0] + b[0], a[1] + b[1])
    return c
