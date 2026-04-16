#!/usr/bin/env python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num_printed_ints = 0
    while i < x:
        try:
            el = my_list[i]
            if isinstance(el, int):
                print("{:d}".format(el))
                num_printed_ints += 1
        except IndexError:
            break
        finally:
            i += 1
    return num_printed_ints
