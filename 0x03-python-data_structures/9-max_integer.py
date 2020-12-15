#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxi = None

    for i in my_list:
        if i > maxi:
            maxi = i
    return maxi
