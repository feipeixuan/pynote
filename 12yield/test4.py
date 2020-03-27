
import asyncio
import inspect

c = ""


async def async1():
    global c
    future = async3()
    await future


async def async3():
    print("2222")


a = async1()
for i in a:
    print(i)
    print("ssss")
    break
for i in c:
    print(i)
    break
for i in a:
    print(i)
print(inspect.getgeneratorstate(a))
# print(a)
