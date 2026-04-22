#!/usr/bin/env python3
"""
Simple python module for Python annotation project
"""


class User():
    """User class definition"""
    def __init__(self, name: str, age: int) -> None:
        """User class constructor"""
        self.name = name
        self.age = age
