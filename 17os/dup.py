import os
import sys


fd = os.open("f1.txt",os.O_RDWR|os.O_CREAT)

# 写入字符串
ret = os.write(fd,"This is runoob.com site".encode("utf-8"))

os.close(sys.stdout.fileno())
new_file = os.dup(fd)
print(new_file)
os.close(fd)
print("22klklkl")
