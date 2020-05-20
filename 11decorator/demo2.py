

class logger:

    def __init__(self,func):
        self.func=func
        self.caches=[]

    def __call__(self, *args, **kwargs):
        print(args)
        self.caches.append(args[0])
        print(self.caches)
        self.func(*args,**kwargs)

class Hello:

    @logger
    def hello(self,name): #logger(Hello.hello) #unbound method
        print(name)

@logger # logger(hello)
def hello(name):
    print(name)

@logger
def hello1(name):
    print(name)

hello("111") #每个方法绑定了自己的装饰器
hello("222")
hello1("333")
hello("444")
a=Hello()
a.hello(a,"33333")