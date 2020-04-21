import os
import sys


file=os.open("22.txt",os.O_CREAT)
os.close(sys.stdout.fileno())
new_file=os.dup(file)
print(2)
os.close(file)