#!/usr/bin/python3
""" declares a class called MagicClass """
import math


class MagicClass:
    """ declaration of __init__ function """
    def __init__(self, radius=0):
        """ initialization of _MagicClass__radius with 0 """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius
    """ defines a function named area """
    def area(self):
        """ returns area """
        return self._MagicClass__radius ** 2 * math.pi
    """ defines a function named circumference """
    def circumference(self):
        """ returns circumference """
        return 2 * math.pi * self._MagicClass__radius
