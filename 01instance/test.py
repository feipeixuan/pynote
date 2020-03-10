# -*- coding: utf-8 -*-
# __new__() 是一种负责创建类实例的静态方法，
# 它无需使用 staticmethod 装饰器修饰，且该方法会优先 __init__() 初始化方法被调用。

class Float_Fail(float):
    def __init__(self, value, unit):
        super().__init__(value)
        self.unit = unit
Float_Fail( 6.5, "knots" )