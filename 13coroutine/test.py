from functools import partial

tasks = []


def add_handler():
    pass


class Future:
    def __init__(self):
        self.call_backs = []

    def add_call_back(self, call_back):
        self.call_backs.append(call_back)

    def execute(self):
        print("执行execute")
        for call_back in self.call_backs:
            call_back()


def add_task(task):
    tasks.append(task)


func = add_task
future = Future()
future.add_call_back(partial(add_task, 2))
future.execute()
print(tasks)

## 偏函数
## functools.partial(func, *args, **keywords)
# func: 需要被扩展的函数，返回的函数其实是一个类 func 的函数
# *args: 需要被固定的位置参数
# **kwargs: 需要被固定的关键字参数


# def partial(func, *args, **keywords):
#     """New function with partial application of the given arguments
#     and keywords.
#     """
#     if hasattr(func, 'func'):
#         args = func.args + args
#         tmpkw = func.keywords.copy()
#         tmpkw.update(keywords)
#         keywords = tmpkw
#         del tmpkw
#         func = func.func
#
#     def newfunc(*fargs, **fkeywords):
#         newkeywords = keywords.copy()
#         newkeywords.update(fkeywords)
#         return func(*(args + fargs), **newkeywords)
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc
