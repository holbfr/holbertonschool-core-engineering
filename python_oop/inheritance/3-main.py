#!/usr/bin/env python3
Square = __import__('1-square').Square

s = Square(13)

print(s)
print(s.area())


try:
    s = Square("13")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
