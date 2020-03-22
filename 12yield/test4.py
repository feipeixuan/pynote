def fun1():
    yield 2
    # print("222")
    # yield 3

def fun2():
    try:
        yield 2
        print("222")
        yield 3
    except GeneratorExit as e:
        print("2222222")
        yield 2


b = fun2()
#print(a.__next__())
b.close()

b = fun2()
print(b.__next__())
b.close()
b.close()
