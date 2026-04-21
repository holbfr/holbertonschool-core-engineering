#!/usr/bin/env python3
"""
Module containing the Rectangle class definition
"""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition"""
    def __init__(self, width, height):
        """Constructor of the Rectangle class"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
