#!usr/bin/env python3
c = __import__('Complejo').Complejo


c1 = c(2, 3)
c2 = c(1, 2)

c3 = c.subtraction(c1, c2)

print(c1)
print(c2)
print(c3)
