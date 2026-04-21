#!/usr/bin/env python3
Square = __import__('2-square').Square
Rectangle = __import__('2-rectangle').Rectangle


s = Square(13)

print(s)
print(s.area())


print("-------------------")


shapes = [Rectangle(3, 5), Square(4)]

for shape in shapes:
    print(shape.area())
