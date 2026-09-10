import asyncio
import time

async def mytask(a,b):
    print(f"任务{a}开始")
    t1=time.time()
    await asyncio.sleep(b)
    print(f"任务{a}结束,耗时{time.time()-t1:6f}秒")

async def main():
    task1=asyncio.create_task(mytask("烧水",2))
    task2=asyncio.create_task(mytask("煮菜",3))
    await task1
    await task2


asyncio.run(main())


async def slow_task(seconds):
    print("任务开始")
    await asyncio.sleep(seconds)
    print("任务结束")
    return "成功"

async def new_main():
    start =time.perf_counter()
    try :
        async with asyncio.timeout(2):
            result=await slow_task(5)
            print(result)
    except TimeoutError:
        print("任务超时")
    end=time.perf_counter()
    print(f"任务耗时{end-start:6f}秒")

asyncio.run(new_main())


