import socket
import os

a, b = socket.socketpair()

id = os.fork()
if id:
    a.close()
    b.send("22".encode())
else:
    b.close()
    print(a.recv(1024))
# socketpair()创建一对未命名的套接字，返回这对套接字描述字于filedes[0]和filedes[1]。套接字偶对是一个全双工的通信通道，在其两端均可执行读和写操作。
#
# 其中domain、type和protocol的解释与套接字函数的相同。但多数系统，包括Linux，只允许domain参数为AF_UNIX；protocol的值常为0，这允许系统使用默认协议。
#
# 如果type指明的是有连接的类型，得到的两个套接字是已连接的。如果type指明了一个无连接的类型，得到的两个套接字是非连接的，但由于它们两者均知道对方，因此可以相互传送消息包。
#
# socketpair()通常用于父子进程之间的通信，它创建的套接字偶对与管道十分类似，其中，一个描述字保留给父进程使用，另一个描述字给子进程使用，父进程关闭子进程使用的描述字，并且需要通过fork()传递其中的一个套接字给子进程，而子进程则需关闭由父进程使用的描述字。