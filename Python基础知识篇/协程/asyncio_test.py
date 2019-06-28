import asyncio


@asyncio.coroutine  # 使用装饰器标识这是一个模型，asyncio要求所有用作协程的生成器必须由asyncio.coroutine装饰
def countdown(number, n):
    while n > 0:
        print('T-minus', n, "({})".format(number))
        yield from asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown('A', 2)),
    asyncio.ensure_future(countdown('B', 5)),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
