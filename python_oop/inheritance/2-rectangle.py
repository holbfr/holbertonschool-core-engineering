#!/usr/bin/env python3
"""
Module containing the Rectangle class definition
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition"""
    def __init__(self, width, height):
        """Constructor of the Rectangle class"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        """"Calculates and return the area value of rectangle"""
        return self.__height * self.__width

    def __repr__(self):
        """String to display of the Rectangle"""
        print("[{}] {}/{}".format(
            self.__class__.__name__,
            self.__width,
            self.__height))

    def __str__(self):
        """String representation of the Rectangle"""
        return "[{}] {}/{}".format(
            self.__class__.__name__,
            self.__width,
            self.__height)
