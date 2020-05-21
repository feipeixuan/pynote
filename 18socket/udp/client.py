#coding=utf-8
from socket import *

#1、创建socket套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#2、准备接收方的地址
sendAddress = ('127.0.0.1',7781)

#3、从键盘输入需要发送的数据
sendData = "kkkk"

#4、发送数据到指定电脑
udpSocket.sendto(sendData.encode(),sendAddress)

#5、等待接收对方发送的数据
receiveData = udpSocket.recvfrom(1024)

#6、显示对方发送的数据
print(receiveData)

#7、关闭socket套接字
udpSocket.close()