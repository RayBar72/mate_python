#!usr/bin/env python3
c = __import__('heron').heron

c1 = c(35, 1)

for x in c1:
    print('{:04f}'.format(x), end=', ')
print()