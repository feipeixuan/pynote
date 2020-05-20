from functools import wraps
def logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__)
        func(*args, **kwargs)

    return inner


@logger
def hello(name):
    print(name)

print(hello.__name__)
# Note
# 此时hello(name) == logger(hello)(name)
# print(hello.__name__) 输出inner
# print(hello.__name__) 输出hello 增加了wrap

# 疑问1 *args 和 **kwargs
# 函数声明：args 是 arguments 的缩写，表示位置参数；kwargs 是 keyword arguments 的缩写，表示关键字参数
# 函数调用：args和kwargs不仅可以在函数定义中使用，还可以在函数调用中使用。在调用时使用就相当于pack（打包）和unpack（解包），类似于元组的打包和解包

# 疑问2 wraps
# 意义：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

# 疑问3 wraps实现
# 参考链接：https://www.cnblogs.com/slysky/p/9777424.html

