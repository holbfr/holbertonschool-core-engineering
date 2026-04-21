#!/usr/bin/env python3
"""Duck Typing task module"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """"Shape Abstract Base Class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle Concrete class"""

    def __init__(self, radius):
        """"Constructor function in class"""
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle Concrete class"""

    def __init__(self, width, height):
        """"Constructor function in class"""
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(my_shape):
    """"Returns shape info of a shape"""
    area = my_shape.area()
    perim = my_shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perim}")
