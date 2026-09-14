from dataclasses import dataclass,field


@dataclass
class RequestConfig:
    method:str = "GET"
    url:str = ""
    timeout:float = 10.0
    headers:dict = field(default_factory=dict)
    params:dict = field(default_factory=dict)
    json_data:dict | None = None

if __name__ == "__main__":
    config = RequestConfig(
        method="POST",
        url="https://example.com",
        timeout=5,
        headers={
            "Authorization": "Bearer xxx"
        },
        json_data={
            "message": "hello"
        }
    )
    print(config)