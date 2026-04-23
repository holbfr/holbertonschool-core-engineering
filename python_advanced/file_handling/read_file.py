#!/usr/bin/env python3
"""
Simple Python module for task validation
"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout"""
    with open(filename, encoding='utf-8') as file:
        print(file.read())
