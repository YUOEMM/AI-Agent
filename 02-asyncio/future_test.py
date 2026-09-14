import asyncio


async def waiter(future):
    print("等待结果...")
    await future
    print("结果:", future.result())


async def produce(future):
    await asyncio.sleep(2)
    print("2秒后...")
    future.set_result("AI Agent")

async def main():
    loop=asyncio.get_running_loop()
    future=loop.create_future()

    task1=asyncio.create_task(waiter(future))
    task2=asyncio.create_task(produce(future))

    await task1
    await task2

asyncio.run(main())