#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            print(my_list[count])
            count += 1
        except IndexError:
            break
    return count
