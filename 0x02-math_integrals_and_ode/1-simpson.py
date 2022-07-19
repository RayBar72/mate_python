#!/usr/bin/env python3
'''Simpson Method and use it to calculate an integral value'''


def simpson_method(a, b, steps):
    '''Simpson Method'''
    if steps % 2 == 0 or steps <= 0:
        raise ValueError('Simpson Method only accepts odd steps and different from zero')
    incr = (b - a) / (steps)
    delt = 0
    x = a
    r = 0
    for i in range(steps + 1):
        y = 1 / (1 + x ** 2)
        if i % 2 == 0 and i != 0 and i != steps:
            y = y * 2
        elif i % 2 != 0 and i != steps:
            y = y * 4
        else:
            y = y
        r += y
        x += incr
    r = (incr / 3) * r
    return r


a = 0
b = 1
steps = 7

print(simpson_method(a, b, steps))
