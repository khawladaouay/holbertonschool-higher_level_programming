#!/usr/bin/python3
from re import A


def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary.keys():
        if key == i:
            a_dictionary.update({i: value})
    a_dictionary[key] = value
    return a_dictionary
