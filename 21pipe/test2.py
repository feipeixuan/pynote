import os

#os.mkfifo("fifo.txt")


file=open("fifo.txt","r")
for content in file:
    print(content)
