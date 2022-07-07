#!usr/bin/env python3
'''Structure “complex” where a complex number a + ib is represented by two doubles'''
import math


class Complejo(object):
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
        if self.im == 0 and self.re ==0:
            return '0'
        elif self.re == 0 and self.im == -1:
            return '-i'.format(self.im)
        elif self.re == 0 and self.im == 1:
            return 'i'.format(self.im)
        elif self.re == 0:
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

    @staticmethod
    def addition(c1, c2):
        '''Deffines addition between two complex numbers'''
        c3 = Complejo(c1.re + c2.re, c1.im + c2.im)
        return c3

    @staticmethod
    def subtraction(c1, c2):
        '''Deffines subtraction between two complex numbers'''
        c3 = Complejo(c1.re - c2.re, c1.im - c2.im)
        return c3

    @staticmethod
    def multiplication(c1, c2):
        '''Deffines multiplication between two complex numbers'''
        x = Complejo(0, 0)
        a = c1.re * c2.re
        b = c1.re * c2.im
        c = c1.im * c2.re
        d = c1.im * c2.im
        x.im = b + c
        x.re = a - d
        return x

    @staticmethod
    def division(c1, c2):
        '''Deffines division between two complex numbers'''
        x = Complejo(c2.re, -c2.im)
        y = Complejo(0, 0)
        div = x.re ** 2 + x.im ** 2
        y = Complejo.multiplication(c1, x)
        # print(x)
        # print(div)
        # print(y)
        y.re = y.re / div
        y.im = y.im / div
        return y

    @staticmethod
    def complex_from_mod_arg(mod, arg):
        '''
        Deffines the complex number from the given argument and modulus.
        Be aware that is not posible to know about results from negative coeficients
        '''
        x = Complejo(0, 0)
        x.re = math.cos(arg) * mod
        x.im = math.sin(arg) * mod
        return x
