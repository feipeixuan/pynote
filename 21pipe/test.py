import os

r, w = os.pipe()

id = os.fork()

if id:
    os.close(w)
    # 创建文件流
    r = os.fdopen(r)
    print("Parent reading")
    for line in r:
        line=line.strip()
        print(line)
    print("Parent end")
else:
    os.close(r)
    os.close(w)
    print("child writing")
    print("child end")
    exit()
    w = os.fdopen(w,'w')
    print("child writing")
    file = open("content.txt","r")
    lines= file.readlines()
    for line in lines:
        w.write(line)

# summary
# 管道只发生在父子进程


# 管道的原子性？？
#