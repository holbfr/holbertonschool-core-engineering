#!/usr/bin/env python3
"""
Simple module containing a Square class definition
"""


class Square:
    """ Simple Square class definition """

    def __init__(self, size=0, position=(0, 0)):
        """ Square class constructor"""
        self.size = size
        self.position = position

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
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for ln in range(self.position[1]):
                    print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """String representation of Square instance"""
        string_repr = ''
        if self.size > 0:
            string_repr += '\n' * self.position[1]
            for i in range(self.size):
                string_repr += ' ' * self.position[0]
                string_repr += self.size * '#'
                if i < self.size - 1:
                    string_repr += '\n'
        return string_repr

    @property
    def position(self):
        """"Position attribute value getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """"Position attribute value setter"""
        is_valid_tuple = (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(item, int) and item >= 0 for item in value)
        )
        if not is_valid_tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
