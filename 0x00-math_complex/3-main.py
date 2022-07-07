#!usr/bin/env python3
c = __import__('3-display').Comp_num


c1 = c(3, 4)
c2 = c(5, -12)
c3 = c(-3, -4)
c4 = c(-5, 12)


print(c1)
print(c1.argument())
print(c2)
print(c2.argument())
print(c3)
print(c3.argument())
print(c4)
print(c4.argument())