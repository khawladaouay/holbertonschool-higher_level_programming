#!/usr/bin/python3
""""this is a Rectangle"""


class Rectangle:
    """"Rectangle class"""
    def __init__(self, width=0, height=0):
        """inisialising"""
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) != int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) != int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width)*2
