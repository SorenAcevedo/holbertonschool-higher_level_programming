#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        end = ""
        for j in range(len(matrix[i])):
            print("{:s}{:d}".format(end, matrix[i][j]), end="")
            end = " "
        print()
