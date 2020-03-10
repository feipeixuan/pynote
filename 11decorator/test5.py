# coding=utf8


# 基于前面的使用函数作为装饰器的理解，将类作为装饰器时需要保证以下几点
#
# 类的实例是可调用的
# 类需要一个地方讲被装饰的函数传入到类的实例里


from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        print("call")
        print(sel)
        return self.func(*args, **kwargs)


@Profiled
def add(x, y):
    return x + y


result = add(1, 2)
print(result)

# add = Profiled(add)
# result = add(1, 2)
# print(result)
#
# 关于 __call__ 方法，不得不先提到一个概念，就是可调用对象（callable），我们平时自定义的函数、内置函数和类都属于可调用对象，但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable
#
# 如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象，
