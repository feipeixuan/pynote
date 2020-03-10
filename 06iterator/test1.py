# -*- coding: utf-8 -*-

class MyArray:

    def __init__(self):
        self.i=10

    def __iter__(self):
        print("sss")
        return self

    def __next__(self):
       while self.i>0:
           yield self.i
           self.i-=1
       raise StopIteration()
obj=MyArray()
list=list(obj.__next__())
print(list)




