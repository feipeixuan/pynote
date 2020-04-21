import os
import sys

os.close(sys.stdin.fileno())
file1=os.open("1.txt",os.O_RDONLY)
print(file1)
os.close(file1)
file1=os.open("2.txt",os.O_RDONLY)
print(file1)