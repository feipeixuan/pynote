#!/usr/bin/env python3
import socket
import time

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1",9500))
    time.sleep(5)
    print(client.send("aaa".encode()))
    print("888")
    # print(client.send("aaa".encode()))

    rs=client.recv(1024)
    if rs:
        print(rs)
    else:
        print("000")
    # data = client.recv(1024)
    # while True:
    #     pass

# print('Received', repr(data))
# 1024 是缓冲区数据大小限制最大值参数 bufsize，
# 并不是说 recv() 方法只返回 1024个字节的内容
