#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement """
        if type(size) != int:
            """ raise an error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size of self with size """
            self.__size = size
