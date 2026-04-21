#!/usr/bin/env python3
"""
Simple module for task validation
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract animal class definition"""

    @abstractmethod
    def sound(self):
        """Abstract sound method"""
        pass


class Dog(Animal):
    """ Dog class definition """

    def sound(self):
        """Sound method for Dog class"""
        return "Bark"


class Cat(Animal):
    """ Cat class definition """

    def sound(self):
        """Sound method for Cat class"""
        return "Meow"

