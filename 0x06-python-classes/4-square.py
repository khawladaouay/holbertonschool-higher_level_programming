#!/usr/bin/python3
"""" this is a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """__init__
        initializing square
        """
        self.__size = size

    @property
    def size(self):
        """ value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """square area"""
        return self.__size*self.__size
