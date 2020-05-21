#coding=utf-8
from socket import *

#1、创建socket套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#2、绑定相关信息，如果一个网络程序不绑定，则系统会随机分配
bindAddress = ('127.0.0.1',7781)#ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddress)

#3、等待接收方发送消息
receiveData = udpSocket.recvfrom(1024)

#4、显示对方发送的数据
print(receiveData)

#5、关闭socket套接字
udpSocket.close()