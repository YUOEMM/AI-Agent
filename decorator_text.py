from functools import wraps
def decor(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("开始执行")
        result=func(*args,**kwargs)
        print("结束执行")
        return result
    return wrapper
@decor
def add(a:int,b:int) ->int:
    return a+b
print(add(3,4))