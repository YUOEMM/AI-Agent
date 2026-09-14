import random

response={
    "headers":{
        "Retry-After":"10"
    }
}

class RetryPolicy:
    def __init__(self,max_attempts=3):
        self.max_attempts=max_attempts
    def should_retry_status(self,status):
        return status in (429,500,502,503,504)
    def get_delay(self,response,attempt):
        if response is not None:
            retry_after=response.get("headers",{}).get("Retry-After")
            if retry_after is not None:
                try:
                    return float(retry_after)
                except ValueError:
                    pass
        return 2**attempt+random.uniform(0,0.5)

policy=RetryPolicy()
print(policy.max_attempts)
print(policy.should_retry_status(500))
print(policy.should_retry_status(404))
print(policy.get_delay(None,0))
print(policy.get_delay(None,1))
print(policy.get_delay(None,2))
print(policy.get_delay(response,0))