#!/usr/bin/env python3
'''Code the Rectangle Method and use it to calculate'''


def rectangle_method(a, b, steps):
    '''Calculates the rectangle_method for a integer'''
    x = a
    s = (b - a) / (steps)
    i = a
    r = 0
    while i < b:
        i += s
        y = (1 / (1 + x ** 2)) * s
        x += s
        r += y
    print(r)


rectangle_method(0, 1, 1000000)