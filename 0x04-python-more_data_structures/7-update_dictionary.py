#!/usr/bin/python3
from re import A


def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        a_dictionary.update({key: value})
    else:
        a_dictionary[key] = value
    return a_dictionary
