#!usr/bin/env python3
'''Structure “complex” where a complex number a + ib is represented by two doubles'''


class Comp_num(object):
    '''A complex number that represents a complex number'''
    def __init__(self, re, im):
        self.re = re
        self.im = im

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, value):
        if type(value) is int or type(value) is float:
            self.__re = value
        else:
            raise ValueError('re must be an int or float')

    @property
    def im(self):
        return self.__im

    @im.setter
    def im(self, value):
        if type(value) is int or type(value) is float:
            self.__im = value
        else:
            raise ValueError('im must be an int or float')

    def __str__(self):
        if self.re == 0:
            return '{}i'.format(self.im)
        elif self.im == 0:
            return '{}'.format(self.re)
        elif self.im < 0:
            return '{} - {}i'.format(self.re, self.im * -1)
        else:
            return '{} + {}i'.format(self.re, self.im)

    def conj(self):
       self.im = -self.im