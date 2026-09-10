class mycontent:
    # 进入上下文管理器时调用
    def __enter__(self):
        print("enter")
        return self
    # 退出上下文管理器时调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        return True

with mycontent() as f:
    print("执行内容")
    print(f)