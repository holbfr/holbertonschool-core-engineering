#!/usr/bin/env python3
"""
Simple Python module for task validation
"""


def write_file(filename="", text=""):
    """Writes a text to the file and returns the number of written chars"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
