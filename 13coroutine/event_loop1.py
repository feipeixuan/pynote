import time
import socket
from functools import partial
from select import *

poll = epoll()
handlers = dict()
scheduled_list = []


def fun():
    print("step1")
    sock = socket.socket()
    future = Future()

    def handler():
        future.set_done(sock.recv(1024))

    add_handler(sock.fileno(), handler, READ)
    yield future
    print("step2")
    yield
    print("step3")
    yield


def add_handler(fd, handler, events):
    handlers[fd] = handler
    # 监听到读事件
    poll.register(fd, events)


class Future(object):

    def __init__(self):
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    # 完成之后，调用回调函数
    def set_done(self, value):
        self.value = value
        for callback in self.callbacks:
            callback()

    def get_result(self):
        return self.value


class Handle(object):
    def __init__(self, gen):
        self.gen = gen

    def call(self):
        yielded = next(self.gen)
        # Fututre 标识未来
        if isinstance(yielded, Future):
            # 添加回调函数
            yielded.add_callback(partial(scheduled_list.append, self))
        else:
            scheduled_list.append(self)


def loop(*coroutines):
    scheduled_list.extend(Handle(c) for c in coroutines)
    while True:

        default_timeout = 10000

        while scheduled_list:
            handle = scheduled_list.pop(0)
            handle.call()

        # 等待描述符可操作
        events = poll.poll(default_timeout)
        while events:
            fd, event = events.popitem()
            # 调用回调函数
            handlers[fd]()
            poll.unregister(fd)
            del handlers[fd]


if __name__ == "__main__":
    loop(fun(), fun(), fun())