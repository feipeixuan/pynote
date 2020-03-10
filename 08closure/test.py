# -*- coding: utf-8 -*-
#
def decorator(c):
    d = 200
    def wrapper(a,b):
        d+=1
        print(c,d)
        return (a+b)*c/d
    return wrapper
wrapper=decorator(150)
wrapper(100,300)
wrapper=decorator(250)
wrapper(100,300)