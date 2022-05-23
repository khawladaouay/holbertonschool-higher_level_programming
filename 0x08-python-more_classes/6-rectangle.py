#!/usr/bin/python3
""""this is a Rectangle"""


class Rectangle:
    """"Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """inisialising"""
        Rectangle.number_of_instances += 1
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

    def print(self):
        if self.__width == 0 or self.__height == 0:
            return print("")
        else:
            for i in range(self.height):
                for i in range(self.width):
                    print("#", end="")

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ("")
        str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str += "#"
            if i < self.__height - 1:
                str += "\n"
        return (str)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
