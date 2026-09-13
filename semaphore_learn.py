import asyncio


current = 0
maximum = 0


async def worker(name, semaphore):
    global current, maximum

    async with semaphore:
        current += 1

        maximum = max(maximum, current)

        print(name, "进入，当前并发：", current)

        await asyncio.sleep(1)

        current -= 1

        print(name, "离开，当前并发：", current)


async def main():
    semaphore = asyncio.Semaphore(3)

    tasks = [
        asyncio.create_task(
            worker(f"任务{i}", semaphore)
        )
        for i in range(10)
    ]

    await asyncio.gather(*tasks)

    print("最大并发数：", maximum)


asyncio.run(main())