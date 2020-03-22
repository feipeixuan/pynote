
async def func_1():
    print("func_1 start")
    print("func_1 end")


async def func_2():
    print("func_2 start")
    print("func_2 a")
    print("func_2 b")
    print("func_2 c")
    print("func_2 end")


f_1 = func_1()
print(f_1)

f_2 = func_2()
print(f_2)


try:
    print('f_1.send')
    f_1.send(None)
except StopIteration as e:
    # 这里也是需要去捕获StopIteration方法
    pass

try:
    print('f_2.send')
    f_2.send(None)
except StopIteration as e:
    pass
from inspect import getgeneratorstate
print(getgeneratorstate(f_2))