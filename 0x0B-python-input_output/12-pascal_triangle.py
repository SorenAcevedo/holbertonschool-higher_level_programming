#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """ triangle """
    if n < 1:
        return []
    l = []
    for i in range(n):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(l[i - 1][j] + l[i - 1][j - 1])
        l.append(temp)

    return l
