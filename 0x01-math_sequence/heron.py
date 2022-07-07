#!usr/bin/env python3
'''
Module that that returns the Heron sequence until having convergence
with an error less or equal to 10 ** -7
'''


def heron(n, inic):
    '''
    Return the n-th order heron sequence.

    Parameters
    ----------
    n : float
        Number which root is been searched.
    inic : float
        Initial number of the recursion'''
    if isinstance(inic, (int, float)) is False or isinstance(n, (int, float)) is False:
        raise TypeError('Invalid input for heron function')
    if inic <= 0 or n <= 0:
        raise ValueError('Invalid input for heron function')
    x = 1
    x0 = inic
    x1 = 0
    reto = []
    while x > .0000001:
        x1 = (x0 + (n / x0)) / 2
        x = abs(x1 - x0)
        x0 = x1
        reto.append(x0)
    return reto