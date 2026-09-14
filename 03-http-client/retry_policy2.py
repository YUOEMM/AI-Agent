import random
from retry_config import RetryConfig


class RetryPolicy:
    def __init__(self,config=None):
        if config is None:
            config=RetryConfig()
        self.config=config
    def should_retry_status(self,status):
        return status in (429,500,502,503,504)
    def get_delay(self,attempt):
        delay=self.config.base_delay*(2**attempt)

        delay=min(delay,self.config.max_delay)

        jitter=random.uniform(0,self.config.jitter)

        return min(delay+jitter,self.config.max_delay)

if __name__ == "__main__":
    config=RetryConfig(
        max_attempts=5,
        base_delay=1.0,
        max_delay=30.0,
        jitter=0.5
    )
    policy=RetryPolicy(config)
    print("最大尝试次数:",policy.config.max_attempts)
    print("最大延迟:",policy.config.max_delay)
    for attempt in range(7):
        print(f"第{attempt}次尝试延迟:{policy.get_delay(attempt):.2f}秒")
