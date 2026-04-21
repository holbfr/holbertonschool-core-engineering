#!/usr/bin/env python3
""""
Module containing the BaseGeometry class definition
"""


class BaseGeometry:
    """BaseGeometry class definition"""
    def __init__(self):
        """BaseGeometry class constructor"""
        pass

    def area(self):
        """Area method that returns a shape's area value"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates that a value represents a valid positive integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
