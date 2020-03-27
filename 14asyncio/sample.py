import types
import select
import time
import socket
import functools


class Future:

    def __init__(self, *, loop=None):
        self._result = None
        self._callbacks = []
        self._loop = loop

    def set_result(self, result):
        self._result = result
        callbacks = self._callbacks[:]
        self._callbacks = []
        for callback in callbacks:
            loop._ready.append(callback)

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def __iter__(self):
        print('enter Future ...')
        print('foo 挂起在yield处 ')
        yield self
        print('foo 恢复执行')
        print('exit Future ...')
        return 'future'

    __await__ = __iter__


class Task:

    def __init__(self, cor, *, loop=None):
        self.cor = cor
        self._loop = loop

    def _step(self):
        cor = self.cor
        try:
            result = cor.send(None)
        # 1. cor 协程执行完毕时，会抛出StopIteration，说明cor执行完毕了，这是关闭loop
        except StopIteration as e:
            self._loop.close()
        # 2. 有异常时
        except Exception as e:
            """处理异常逻辑"""
        # 3. result为Future对象时
        else:
            if isinstance(result, Future):
                result.add_callback(self._wakeup)

    def _wakeup(self):
        self._step()


class Loop:

    def __init__(self):
        self._stop = False
        self._ready = []
        self._scheduled = []
        self._time = lambda: time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        self._select = functools.partial(select.select, [sock], [], [])

    def create_task(self, cor):
        task = Task(cor, loop=self)
        self._ready.append(task._step)
        return task

    def call_later(self, delay, callback, *args):
        callback._when = delay
        self._scheduled.append((callback, *args))

    def run_until_complete(self, task):
        assert isinstance(task, Task)
        timeout = None

        while not self._stop:

            if self._ready:
                timeout = 0

            if self._scheduled:
                callback, *args = self._scheduled.pop()
                timeout = callback._when
                self._ready.append(functools.partial(callback, *args))

                # 通过select(timeout)来控制阻塞时间
                self._select(timeout)

            n = len(self._ready)

            for i in range(n):
                step = self._ready.pop()
                step()

    def close(self):
        self._stop = True


@types.coroutine
def _sleep():
    yield


# 自己实现一个sleep协程
async def sleep(s, result=None):
    if s <= 0:
        await _sleep()
        return result
    else:
        future = Future(loop=loop)
        future._loop.call_later(s, callback, future)
        await future
        print("state1")
        return result


# 延迟回调函数
def callback(future):
    # 时间到了就回调此函数
    future.set_result(None)


async def foo():
    print(f'enter foo at {time.strftime("%Y-%m-%d %H:%M:%S")}')
    await sleep(3)
    print(f'exit foo  at {time.strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == '__main__':
    f = foo()
    loop = Loop()
    task = loop.create_task(f)
    loop.run_until_complete(task)