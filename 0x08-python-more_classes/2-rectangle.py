#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initizie width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates and returns area """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of a Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
