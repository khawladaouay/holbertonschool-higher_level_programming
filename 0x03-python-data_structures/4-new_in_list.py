#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    for i in my_list:
        newlist.append(i)
    if idx < 0:
        return newlist
    elif len(my_list) - 1 < idx:
        return newlist
    else:
        newlist[idx] = element
        return newlist
