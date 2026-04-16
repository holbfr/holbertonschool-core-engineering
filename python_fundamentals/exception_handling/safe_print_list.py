#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(my_list):
        try:
            print(my_list[i])
            count += 1
        except IndexError:
            pass
    return count
