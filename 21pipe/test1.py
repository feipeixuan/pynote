import os
import sys

r, w = os.pipe()

id = os.fork()

if id:
    os.close(w)
    os.close(sys.stdin.fileno())
    # 创建文件流
    r = os.fdopen(r)
    os.dup(r.fileno())
    print("Parent reading")
    for line in r:
        line=line.strip()
        print(line)
else:
    os.close(r)
    w = os.fdopen(w,'w')
    print("child writing")
    file = open("content.txt","r")
    os.close(sys.stdout.fileno())
    os.dup(file.fileno())
    lines= file.readlines()
    for line in lines:
        w.write(line)