#写一个时间装饰器
#输出类似:
#开始执行
#HELLO AGENT
#执行耗时:0.0000xxx秒
import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("开始执行")
        t1=time.time()
        result=func(*args,**kwargs)
        t2=time.time()
        print(f"执行耗时:{t2-t1:6f}")
        return result
    return wrapper


@timer
def print_():
    print("HELLO AGENT")


print_()