#!/usr/bin/python3
"""
Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides matrix """

    ex_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    for i in matrix:
        if type(i) != list or not all(type(j) in (int, float) for j in i):
            raise TypeError(ex_1)

    if not all(len(matrix[0]) == len(j) for j in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in (int, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    nm = list(map(lambda b: list(map(lambda x: round(x / div, 2), b)), matrix))
    return nm
