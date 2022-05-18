#!/usr/bin/python3
"""" this is a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__
        initializing square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        k = 0
        if self.__size == 0:
            print()
            return None
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                while k < self.__position[0]:
                    print(' ', end='')
                    k += 1
                print('#', end='')
            k = 0
            print()
