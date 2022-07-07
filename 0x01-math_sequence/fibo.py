#!/usr/bin/env python3
'''Structure that contains function for fibonacci series'''


def fibo():
    gold = 1.618034
    fi = []
    x0 = 0
    x1 = 1
    y = 1
    while y >= 0.0000001:
        x2 = x1 + x0
        fi.append(x2)
        y = abs(gold - x2 / x1)
        x0 = x1
        x1 = x2
    return fi


x = fibo()

print(', '.join(map(str, x)))
