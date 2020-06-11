#coding=utf-8
import json
from socket import *


#1、创建socket套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#2、绑定相关信息，如果一个网络程序不绑定，则系统会随机分配
bindAddress = ('127.0.0.1',7781)#ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddress)
users=dict()

while True:
    udp_data,address = udpSocket.recvfrom(1024)
    data = json.loads(udp_data.decode())
    name = data['name']
    msg = data['msg']
    new_msg =None
    if name not in users:
       users[name] = address
       new_msg = json.dumps({'name': '系统', 'msg':'{0}进入了聊天室'.format(name)})
    print(users.keys())
    for local_name,local_address in users.items():
        print(local_address)
        if name==local_name:
            continue
        if new_msg is not None:
            udpSocket.sendto(new_msg.encode(), local_address)

        json_data = json.dumps({'name': name, 'msg': msg})
        udpSocket.sendto(json_data.encode(), local_address)


