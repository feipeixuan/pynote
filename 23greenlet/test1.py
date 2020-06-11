from greenlet import greenlet,getcurrent


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
    print(getcurrent)


def test2():
    print(56)
    gr1.switch()
    greenlet(test3).switch()
    print(78)

def test3():
    print("test3sss")

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print(gr1.dead)
print(gr2.dead)
print(dir(greenlet)) # 返回属性列表