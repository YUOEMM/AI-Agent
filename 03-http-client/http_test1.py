# 10 个 HTTP 请求
#        ↓
# Semaphore(3)
#        ↓
# 同时最多3个
#        ↓
# 每个请求有 timeout
#        ↓
# 统计：
# 成功几个
# 失败几个
# 总耗时多少
import asyncio
import httpx
import time

sem=asyncio.Semaphore(3)

async def request(client,i):
    for attempt in range(3):

        async with sem:
            try:
                response=await client.get("https://httpbin.org/get")
                print(f"请求{i} 状态码：{response.status_code}")
                return response.status_code #正确位置
            except Exception as e:
                if attempt<2:
                    print(f"第{i}次失败,第{attempt + 1}次重试")
                    await asyncio.sleep(2**attempt)
                else:
                    print(f"第{i}次失败,重试3次,失败")
                    return None
        # return response.status_code  错误1


async def main():
    start=time.perf_counter()
    timeout=httpx.Timeout(3)

    async with httpx.AsyncClient(timeout=timeout) as client:
        #tasks = [request(client,i) for i in range(10)]
        tasks = [asyncio.create_task(request(client,i)) for i in range(10)]

        results=await asyncio.gather(*tasks,return_exceptions=True)#return_exceptions=True 多余 3
    end=time.perf_counter()
    print(results)
    print(f"成功:{results.count(200)}")
    print(f"失败:{len(results)-results.count(200)}")
    print(f"耗时：{end-start:.2f} 秒")


asyncio.run(main())