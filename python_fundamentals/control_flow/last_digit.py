#!/usr/bin/env python3
  
  
number = __import__('random').randint(-10000, 10000)

if number >= 0:
    r = number % 10
else:
    r = number % -10
if r > 5:
    m = "and is greater than 5"
elif r == 0:
    m = "and is 0"
elif r < 6 and r != 0:
    m = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, r, m))
