from functools import wraps

# 带参数的装饰器
def logger(num):
    def inner1(func):
        def inner(*args,**kwargs):
            for i in range(num):
                print(func.__name__)
            func(*args,**kwargs)
        return inner
    return inner1



@logger(num=2) # logger(2)(hello)
def hello(name):
    print(name)

hello("222") # logger(2)(hello)("222")