#!/usr/bin/python3
def matrix_divided(matrix, div):
    for i in matrix:
        if not isinstance(i, (float, int)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != matrix[1]:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int or type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        ZeroDivisionError("division by zero")
    mat = []
    for i in matrix:
        mat.append(list(map(lambda x: round(x / div, 2), row)))
    return mat
    