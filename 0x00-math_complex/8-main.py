#!usr/bin/env python3
c = __import__('Complejo').Complejo


c1 = c(2, 2)
mod = c1.modo()
arg = c1.argument()
c2 = c.complex_from_mod_arg(mod, arg)
print(c1)
print(c2)
