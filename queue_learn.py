import asyncio


async def producer(queue):
    for i in range(10):
        await queue.put(f"任务-{i}")
        print("生产：", f"任务-{i}")


async def worker(name, queue):
    while True:
        task = await queue.get()

        print(name, "开始处理", task)

        await asyncio.sleep(2)

        print(name, "完成", task)

        queue.task_done()


async def main():
    queue = asyncio.Queue()

    workers = [
        asyncio.create_task(worker("Worker-1", queue)),
        asyncio.create_task(worker("Worker-2", queue)),
        asyncio.create_task(worker("Worker-3", queue)),
    ]

    await producer(queue)

    await queue.join()

    for worker_task in workers:
        worker_task.cancel()


asyncio.run(main())