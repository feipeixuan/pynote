import sys

b=12
print sys.getrefcount(b)
ab=b
c=b
print sys.getrefcount(ab)
del b
print sys.getrefcount(ab)