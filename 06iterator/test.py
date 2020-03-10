# -*- coding: utf-8 -*-

class MyArray:

    def __init__(self):
        self.i=10

    def __iter__(self):
        print("sss")
        return self

    def __next__(self):
        if(self.i<0):
            raise StopIteration()
        self.i-=1
        return self.i
obj=MyArray()
for value in obj:
    print(value)




