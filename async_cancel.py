import asyncio

async def work():

    try:

        print("任务开始")

        await asyncio.sleep(10)

        print("任务完成")

    except asyncio.CancelledError:

        print("work：收到取消信号")

        raise # 抛出取消异常,如果没有,下面的except捕获不到取消异常


async def main():

    task = asyncio.create_task(work())

    await asyncio.sleep(2)

    print("main：准备取消")

    task.cancel()

    try:

        await task

    except asyncio.CancelledError:

        print("main：确认任务已经取消")


asyncio.run(main())