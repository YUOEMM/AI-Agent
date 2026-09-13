import asyncio
import httpx
import time
import random

sem=asyncio.Semaphore(3)

def should_retry(status):
    return status in (429,500,502,503,504)
def get_retry_delay(response,attempt):
    if response is not None:
        if response.headers.get("Retry-After"):
            try:
                return float(response.headers.get("Retry-After"))
            except ValueError:
                pass

    return 2**attempt+random.uniform(0,0.5)


async def request(client,i):
    for attempt in range(3):
        response = None

        try:
            async with sem:
                response=await client.get("https://httpbin.org/status/500")
            print(f"第{i}个请求,状态码{response.status_code}")
            response.raise_for_status()
            print(f"请求{i}成功")
            return response.status_code
        except httpx.TimeoutException:
            print(f"第{i}个请求超时")
            print("准备重试")
        except httpx.HTTPStatusError as e:
            if should_retry(e.response.status_code):
                print(f"请求{i}收到可重试编码,准备重试")
            else:
                print(f"请求{i}收到不重试编码,退出请求")
                return None
        if attempt <2:
            delay=get_retry_delay(response,attempt)
            print(f"请求{i}第{attempt+1}次重试,等待时间{delay:.2f}")

            await asyncio.sleep(delay)

        else:
            print(f"请求{i}最终失败")
            return None


async def main():
    start=time.perf_counter()
    timeout=httpx.Timeout(3)

    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks = [asyncio.create_task(request(client,i)) for i in range(10)]
        results=await asyncio.gather(*tasks)
    end=time.perf_counter()
    print(results)
    print(f"成功:{results.count(200)}")
    print(f"失败:{len(results)-results.count(200)}")
    print(f"耗时：{end-start:.2f} 秒")


asyncio.run(main())