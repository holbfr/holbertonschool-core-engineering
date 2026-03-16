#!/usr/bin/env python3

def print_last_digit(number):
    if number >= 0:
        r = number % 10
        print("{:d}".format(r), end="")
        return r
    else:
        r = (number % -10) * -1
        print("{:d}".format(r), end="")
        return r
