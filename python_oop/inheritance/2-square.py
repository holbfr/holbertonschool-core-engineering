#!/usr/bin/env python3
"""
Module contains Square class definition
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition"""
    def __init__(self, size):
        """Square class definition"""
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Square area value"""
        return self.__size ** 2

    def __repr__(self):
        """String representation of Square"""
        print("[Square] {}/{}".format(self.__size, self.__size))

    def __str__(self):
        """Strin representation of Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
