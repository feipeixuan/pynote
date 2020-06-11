#!/usr/bin/env python3
import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind(("127.0.0.1",9500))
    server.listen(1)
    conn, addr = server.accept()
    with conn:
        print('Connected by', addr)
        # conn.sendall("kkkk".encode("utf-8"))
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)

# 这个程序只能服务于一个客户端然后结束。
# 和 send() 方法不一样的是，sendall() 方法会一直发送字节，只到所有的数据传输完成 或者中途出现错误。

# send 和 sendall的区别
# socket.send(string[, flags]) 　
# 发送TCP数据，返回发送的字节大小。这个字节长度可能少于实际要发送的数据的长度。换句话说，这个函数执行一次，并不一定能发送完给定的数据，可能需要重复多次才能发送完成
# data = "something you want to send"
# while True:
# 	len = s.send(data[len:])
# 	if not len:
# 		break


# 到目前为止，我们有两个问题：
# 1.如何同时处理多个连接请求
# 2.我们需要一直调用 send() 或者 recv() 直到所有数据传输完成