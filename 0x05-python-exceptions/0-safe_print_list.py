#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = 0
        for i in range(0, x):
            print(my_list[i], end="")
            length += 1
        print("")
        return x
    except IndexError:
        print("")
        return length
