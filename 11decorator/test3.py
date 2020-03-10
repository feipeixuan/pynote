

# 使用场景
# 现在我们来看一下装饰器在哪些地方特别耀眼，以及使用它可以让一些事情管理起来变得更简单。
#
# 授权(Authorization)
# 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权


# 日志(Logging)
# 日志是装饰器运用的另一个亮点。这是个例子：

from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
# Output: addition_func was called

# 开发原则 ： 开放封闭原则
# 装饰器的作用 ：在不改变原函数的调用方式的情况下，在函数的前后添加功能
# 装饰器的本质 ： 闭包函数