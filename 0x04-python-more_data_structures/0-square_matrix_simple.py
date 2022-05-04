#!/usr/bin/python3
def square(num):
    return num*num


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        matrix_square = list(map(square, i))
        new_matrix.append(matrix_square)
    return new_matrix
