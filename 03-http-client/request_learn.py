import requests
response = requests.get("https://www.baidu.com")
print(response.status_code)
print(response.text)
print(response.content)

date={
    "name":"AI Agent",
    "age":18,
}


response=requests.post("https://httpbin.org/post",
                       json=date)
print(response.status_code)
print(response.json())