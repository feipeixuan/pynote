# -*- coding: utf-8 -*-

i=2

def test1():
    """
    下面語句一定要聲明
    """
    global i
    i+=1
    print(i)

test1()
a=test1
print(a)
print(type(a))
print(a.__doc__)
#返回当前范围内的变量、方法和定义的类型列表
print(dir(a))
print(a.__dict__)
print(a.__code__)