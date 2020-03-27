# coding=utf8
class Person:

    type=2

    def __init__(self):
        self.name=2

# 优先在实例属性中搜索找不到就去类属性进行搜索
print(Person().type)