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
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) != int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter attribute
        """
        if type(value) != int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        else:
            self.__height = value
