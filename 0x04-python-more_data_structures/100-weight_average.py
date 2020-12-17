#!/usr/bin/python3
def mul(t=()):
    c = 1
    for i in t:
        c *= i
    return c


def weight_average(my_list=[]):
    if my_list:
        return sum([mul(i) for i in my_list]) / sum([i[1] for i in my_list])
    return 0
