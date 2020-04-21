import os

file = os.open("1.txt", os.O_RDONLY)
os.lseek(file,2,0)
print(os.fstat(file))
value = os.read(file, 100)
value = bytes.decode(value)
print(value)
print(type(value))
print(value)

