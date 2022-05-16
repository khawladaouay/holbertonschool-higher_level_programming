#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = [0] * list_length
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            list[i] = result
        except ArithmeticError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return list
