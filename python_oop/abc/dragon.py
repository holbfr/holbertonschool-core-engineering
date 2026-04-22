#!/usr/bin/env python3
"""
Simple module for task validation
"""


class SwinMixin():
    """SwinMixin class definition"""
    def swim(self):
        """Prints the creature swims"""
        print("The creature swims!")


class FlyMixin():
    """FlyMixin class definition"""
    def fly(self):
        """Prints the creature can fly"""
        print("The creature flies!")


class Dragon(SwinMixin, FlyMixin):
    """Dragon class definition"""
    def roar(self):
        """Prints the creature roaring"""
        print("The dragon roars!")
