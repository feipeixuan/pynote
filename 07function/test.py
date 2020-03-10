# -*- coding: utf-8 -*-

i=2

def test1():
    #  下面語句一定要聲明
    global i
    i+=1
    print(i)

test1()