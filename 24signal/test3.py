import signal
import os
import fcntl
import time


def test1(*args):
    print(args[0])
    print(args[1])
    exit()

signal.signal(signal.SIGIO,test1)
f=os.open("1.txt",os.O_RDONLY)

print(f)
fcntl.fcntl(0,fcntl.F_SETOWN, os.getpid())
fcntl.fcntl(0,fcntl.F_SETFL, os.O_ASYNC|os.O_NONBLOCK)
try:
    input()
except Exception as e:
    pass
while True:
    try:
        time.sleep(1)
    except Exception as e:
        pass
