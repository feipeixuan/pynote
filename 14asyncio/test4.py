import asyncio


async def test1():
    print("1")
    await asyncio.sleep(1)  # asyncio.sleep(1)返回的也是一个协程对象
    print("2")


async def test2():
    print("3")
    print("4")


a = test1()
b = test2()
print(a)
print(b)

loop = asyncio.get_event_loop()
tasks = asyncio.gather(a,b)
print(asyncio.all_tasks(loop))
task_state=asyncio.all_tasks(loop)
loop.run_until_complete(tasks)
