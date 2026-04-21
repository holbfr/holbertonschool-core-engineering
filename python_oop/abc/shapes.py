#!/usr/bin/env python3
"""
Simple module for task validation
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape ABC definition"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class definition"""
    def __init__(self, radius):
        """Circle class constructor"""
        self.radius = radius

    def area(self):
        """Circle area value"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Circle perimeter value"""
        return math.pi * self.radius * 2


class Rectangle(Shape):
    """Rectangle class definition"""
    def __init__(self, width, height):
        """Rectangle class constructor"""
        self.width = width
        self.height = height

    def area(self):
        """Rectangle area value"""
        return self.height * self.width

    def perimeter(self):
        """Rectangle perimeter value"""
        return 2 * (self.height + self.width)


def shape_info(shape):
    """Prints shape area and perimeter values"""
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
