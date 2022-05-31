#!/usr/bin/python3
""""read_file module"""


def read_file(filename=""):
    """"reaf_file function
    this function reads file with 'filename'
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
