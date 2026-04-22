#!/usr/bin/env python3
"""
Simple module for task validation
"""


class Fish():
    """Fish class definition"""

    def swim(self):
        """Prints the fish swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Prints where the fish lives"""
        print("The fish lives in water")


class Bird():
    """Bird class definition"""

    def fly(self):
        """Prints the bird flying"""
        print("The bird is flying")

    def habitat(self):
        """Prints where the bird lives"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class definition"""

    def fly(self):
        """Prints the bird flying"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints where the bird lives"""
        print("The flying fish lives both in water and the sky!")

    def swim(self):
        """Prints the fish swimming"""
        print("The flying fish is swimming!")
