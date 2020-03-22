import asyncio

#使用async关键字定义一个协程，协程也是一种对象，不能直接运行，需要加入事件循环中，才能被调用
async def func_1():
    print("func_1 start")
    print("func_1 end")
    # await asyncio.sleep(1)


async def func_2():
    print("func_2 start")
    print("func_2 a")
    print("func_2 b")
    print("func_2 c")
    print("func_2 end")
    # await asyncio.sleep(1)



# 获取 EventLoop:
loop = asyncio.get_event_loop()
tasks = [func_1(), func_2()]

# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()