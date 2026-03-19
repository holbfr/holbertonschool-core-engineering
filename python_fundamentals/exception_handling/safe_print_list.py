#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    max = x
    if x > len(my_list):
        max = len(my_list)
    for i in range(max):
        print(my_list[i])
