#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]

    l1 = len(tuple_a)
    if l1 >= 2:
        l1 = 2
    l2 = len(tuple_b)
    if l2 >= 2:
        l2 = 2

    for i in range(l1):
        a[i] = tuple_a[i]
    for i in range(l2):
        b[i] = tuple_b[i]

    c = (a[0] + b[0], a[1] + b[1])
    return c
