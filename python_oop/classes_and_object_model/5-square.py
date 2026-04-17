#!/usr/bin/env python3
"""
Simple module containing a Square class definition
"""


class Square:
    """ Simple Square class definition """

    def __init__(self, size=0):
        """ Square class constructor"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (value is not None) and (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif not (value >= 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method returns the value area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square to the stdout"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print(self.size * '#')
