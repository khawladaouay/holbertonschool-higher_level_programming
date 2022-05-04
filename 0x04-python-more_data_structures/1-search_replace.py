#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    for i in my_list:
        if i == search:
            newlist[newlist.index(i)] = replace
    return newlist
