

def fun1():
    try:
        yield 2
        print("222")
        yield 3
    except Exception as e:
        print("ece")
        pass
    yield 3


a=fun1()
print(a.__next__())
print(a.throw(Exception("222")))