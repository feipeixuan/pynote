
class Base1(object):

    def __init__(self):
        self.__name1="333"
        self.__name2__="fei"

obj=Base1()
print(obj.__dict__)
print(obj._Base1__name1)