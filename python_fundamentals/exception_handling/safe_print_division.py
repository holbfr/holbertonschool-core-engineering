#!/usr/bin/env python3


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("division by 0")
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
