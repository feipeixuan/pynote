#coding=utf-8
import random
import json
from concurrent.futures import ThreadPoolExecutor
from socket import *

class UdpClient:

    def __init__(self):

        # 1、创建socket套接字
        self.udpSocket = socket(AF_INET, SOCK_DGRAM)

        # 2、准备接收方的地址
        self.sendAddress = ('127.0.0.1', 7781)

        self.name= "马里奥"+str(random.randint(1, 5000))

        self.flag=True

    def receive(self):
        while True:
            data,addr = self.udpSocket.recvfrom(1024)
            data = json.loads(data.decode())
            print(data)
            name = data['name']
            msg = data['msg']
            print("收到{0} : {1}".format(name,msg))




    def send(self):
        while True:
            data = input("input")
            udp_data = json.dumps({'name': self.name, 'msg': data})
            self.udpSocket.sendto(udp_data.encode(), self.sendAddress)
            # data,addr = self.udpSocket.recvfrom(1024)
            # data = json.loads(data.decode())
            # print(data)
            if "exit" in data:
                self.flag=False
                break


client=UdpClient()
executor = ThreadPoolExecutor(max_workers=2)
executor.submit(client.receive)
executor.submit(client.send)