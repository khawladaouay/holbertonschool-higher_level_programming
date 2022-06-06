#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method
        this method initializes on instance creation
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area Method
        this method will calculate the rectangle object's area
        """
        return self.height * self.width

    def display(self):
        """display Method
        this method will display the rectangle
        """
        for j in range(self.y):
            print("")

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """__str__ method
        this method will print the rectangle on print() or str()
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update Method
        this method will assign a key/value argument to attributes
        """
        argc = len(args)
        kwargc = len(kwargs)
        my_list = ["id", "width", "height", "x", "y"]
        if argc > 0:
            if argc > len(my_list):
                argc = len(my_list)
            for i in range(argc):
                setattr(self, my_list[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                if key in my_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary Method
        this method will return the dictionary representation of a Rectangle
        """
        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
