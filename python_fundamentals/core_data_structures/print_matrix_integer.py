#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        ln = len(row)
        for i in range(ln):
            print("{:d}".format(row[i]), end=" " if i < ln - 1 else "")
        print()
