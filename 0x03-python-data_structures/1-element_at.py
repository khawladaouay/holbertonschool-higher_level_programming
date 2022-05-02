#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        elif len(my_list) - 1 < idx:
            return None
        else:
            return my_list[idx]
