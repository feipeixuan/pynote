import socket
import os
from signal import *
from multiprocessing import *

def talk(conn):
    os.getpid()
    while 1:  # 循环通讯
        try:
            from_client_msg = conn.recv(1024)
            if not from_client_msg:
                break
            print("进程<%s>来自客户端的消息:%s" % (os.getpid(), from_client_msg))
            conn.send(from_client_msg.upper())
        except:
            break
    conn.close()

signal(SIGCHLD,SIG_IGN)
# signal.SIGCHLD Child process stopped or terminated
#signal.SIG_IGN¶ 这是另一个标准信号处理程序，它将简单地忽略给定的信号。
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind(("127.0.0.1", 9500))
    server.listen(2)
    while True:
        conn, addr = server.accept()
        process = Process(target=talk, args=(conn,))
        process.start()
        conn.close()
        process.join()


