# -*- coding: utf-8 -*-

a=( i for i in range(4))
for j in a:
    print(j)
print(a.__next__())
print(a.__next__())
print(a.__next__())
