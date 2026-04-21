#!/usr/bin/env python3
"""
Module contains Square class definition
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition"""
    def __init__(self, size):
        """Square class definition"""
        super().__init__(size, size)
        self.__size = super().integer_validator("size", size)

    def area(self):
        """Square area value"""
        return self.__size ** 2
