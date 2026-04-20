#!/usr/bin/env python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num_printed_ints = 0
    while i < x:
        try:
            el = my_list[i]
            if isinstance(el, int):
                print("{:d}".format(el), end='')
                num_printed_ints += 1
        except Exception as e:
            print(e.message)
        finally:
            i += 1
    print()
    return num_printed_ints
