#!/usr/bin/env python3
"""
Simple module containing a Square class definition
"""


class Square:
    """ Simple Square class definition """

    def __init__(self, size=0):
        """ Square class constructor"""
        if (size is not None) and (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif not (size >= 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method returns the value area of the square"""
        return self.__size ** 2
