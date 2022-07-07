#!usr/bin/env python3
'''Structure “complex” where a complex number a + ib is represented by two doubles'''
import math


class Comp_num(object):
    '''A complex number that represents a complex number'''
    def __init__(self, re, im):
        '''Constructor'''
        self.re = re
        self.im = im

    @property
    def re(self):
        '''Deffines the real number to a complex number'''
        return self.__re

    @re.setter
    def re(self, value):
        '''Set the real number to a complex number'''
        if type(value) is int or type(value) is float:
            self.__re = value
        else:
            raise ValueError('re must be an int or float')

    @property
    def im(self):
        '''Deffines the imaginary number to a complex number'''
        return self.__im

    @im.setter
    def im(self, value):
        '''Set the imaginary number to a complex number'''
        if type(value) is int or type(value) is float:
            self.__im = value
        else:
            raise ValueError('im must be an int or float')

    def __str__(self):
        '''Deffines the complex number to a string'''
        if self.re == 0:
            return '{}i'.format(self.im)
        elif self.im == 0:
            return '{}'.format(self.re)
        elif self.im < 0:
            return '{} - {}i'.format(self.re, self.im * -1)
        elif self.im == 1:
            return '{} + i'.format(self.re, self.im * -1)
        elif self.im == - 1:
            return '{} - i'.format(self.re, self.im * -1)
        else:
            return '{} + {}i'.format(self.re, self.im)

    def conj(self):
        '''Deffines the conjugate number to a complex number'''
        self.im = -self.im

    def modo(self):
        '''Deffines the modulus number to a complex number'''
        return (self.im ** 2 + self.re ** 2) ** (1 / 2)

    def argument(self):
        '''Deffines the argument number to a complex number'''
        if self.im < 0 and self.re < 0:
            a = math.atan(abs(self.im) / abs(self.re))
            return - (math.pi - a)
        if self.im > 0 and self.re < 0:
            a = math.atan(abs(self.im) / abs(self.re))
            return (math.pi - a)
        elif self.im < 0 and self.re > 0:
            a = math.atan(abs(self.im) / abs(self.re))
            return (- a)
        else:
            return(math.atan(abs(self.im) / abs(self.re)))
