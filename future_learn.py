import asyncio
#future.set_result(value)
#future.set_exception(error)
#future.cancel()
#future.done()
#future.cancelled()
#future.result()




async def main():
    # 获取当前正在运行的事件循环（Event Loop）
    # 事件循环是 asyncio 的核心，负责调度和执行协程、Future、Task 等
    loop = asyncio.get_running_loop()

    # 创建一个 Future 对象
    # Future 是一个"未来的结果占位符"，它代表一个尚未完成的异步操作
    # 初始状态为"未完成（pending）"，可通过 set_result() 或 set_exception() 使其变为"已完成"
    future = loop.create_future()

    # future.done() 返回 False，因为此时 Future 还没有被设置结果
    print("完成前：", future.done())

    # 为 Future 设置一个成功结果，这会将其状态从 pending 变为 finished
    # 任何正在 await 这个 future 的协程都会被唤醒并拿到这个值
    future.set_result("hello")

    # future.done() 返回 True，因为上面已经调用 set_result 设置了结果
    print("完成后：", future.done())

    # future.result() 获取 Future 中存储的结果值，即 "hello"
    # 如果 Future 是被 set_exception() 完成的，这里会抛出对应的异常
    print("结果：", future.result())

# asyncio.run() 创建一个新的事件循环，运行 main() 协程，直到它结束
asyncio.run(main())