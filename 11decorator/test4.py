# coding=utf8

# 带参数的装饰器只需要在原来那个不带参数的装饰器基础上之上在最外层套一个函数，该函数中定义一个参数，然后嵌套函数中引用该参数即可实现

from functools import wraps


def test1(value):

    def _test1(func):
        @wraps(func)
        def wrapped_function():
            print("before")
            print(value)
            func()
            print("after")

        return wrapped_function
    return _test1



@test1(value=2)
def test2():
    print("sssss")



print(test2.__name__)

