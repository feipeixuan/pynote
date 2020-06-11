import signal
import time
import sys
import os

def handle_int(sig, frame):
    print("get signal: %s, I will quit"%sig)
    sys.exit(0)

def handle_hup(sig, frame):
    print("get signal: %s"%sig)


if __name__ == "__main__":
    # ctrl+c事件和 SIGHUP，也就是 1 和 2 信号
    signal.signal(2, handle_int) #signal.signal() 函数允许定义在接收到信号时执行的自定义处理程序
    signal.signal(1, handle_hup)
    print("My pid is %s"%os.getpid())
    while True:
        time.sleep(3)

# signal.signal(signalnum, handler)
# signalnum 为某个信号，handler 为该信号的处理函数。
# 进程可以无视信号，可以采取默认操作，还可以自定义操作。
# 当 handler 为 signal.SIG_IGN 时，信号被无视（ignore）；当 handler 为 singal.SIG_DFL，进程采取默认操作（default）；
# 当 handler 为一个函数名时，进程采取函数中定义的操作。

# My pid is 22861
# get signal: 1
# get signal: 2, I will quit