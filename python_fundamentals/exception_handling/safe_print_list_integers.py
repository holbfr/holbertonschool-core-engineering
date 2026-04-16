#!/usr/bin/env python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            if type(my_list[count]) is int:
                print(my_list[count])
            count += 1
        except IndexError:
            break
    return count
