#!usr/bin/env python3
c = __import__('heron').heron

c1 = c(35, 1)

print(', '.join(map(str, c1)))
