#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda b: list(map(lambda x: x*x, b)), matrix))
