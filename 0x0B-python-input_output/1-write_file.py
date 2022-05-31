#!/usr/bin/python3
""""write_file module"""


def write_file(filename="", text=""):
    """"write_file function that writes a string to  text file"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
