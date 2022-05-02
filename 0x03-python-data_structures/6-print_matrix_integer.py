#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        size = len(i)
        last = 1
        for n in i:
            if size == last:
                print(f"{n}", end='')
            else:
                print(f"{n} ", end='')
            last = last + 1
        print("")
