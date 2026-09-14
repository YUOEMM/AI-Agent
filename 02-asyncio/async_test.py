import asyncio
import time
# 1. 定义一个异步任务
async def work(name, seconds):
    print(f"{name}：开始执行")
    # 模拟网络请求 / API 请求
    # await 会把执行权交还给 Event Loop
    await asyncio.sleep(seconds)
    print(f"{name}：执行完成")
    # 返回结果
    return f"{name}完成"

# 2. 主协程
async def main():

    start = time.perf_counter()

    print("=== 开始 ===")

    # 创建两个协程对象
    coroutine_a = work("任务A", 2)
    coroutine_b = work("任务B", 3)
    print("Coroutine 已经创建")

    # 3. 使用 gather 并发执行
    results = await asyncio.gather(
        coroutine_a,
        coroutine_b
    )
    # 4. 输出结果
    print("所有任务完成")

    print("结果：")
    print(results)

    # 5. 计算总耗时
    end = time.perf_counter()

    print(f"总耗时：{end - start:.2f} 秒")

# 6. 启动 Event Loop
asyncio.run(main())