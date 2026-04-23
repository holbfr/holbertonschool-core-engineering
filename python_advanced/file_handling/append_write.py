#!/usr/bin/env python3
"""
Simple Python module for task validation
"""


def append_write(filename="", text=""):
    """Append text to a file and returns the number of added characters"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
