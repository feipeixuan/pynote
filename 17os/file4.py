import os

f1=os.open("1.txt",os.O_RDONLY)
f2=os.dup(f1)
print(os.read(f1,1))
print(os.read(f2,1))
print(os.read(f1,1))