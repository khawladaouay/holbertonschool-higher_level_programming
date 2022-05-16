#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resul = a/b
        return resul
    except ZeroDivisionError:
        resul = None
        return resul
    finally:
        print("Inside result: {}".format(resul))
