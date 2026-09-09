def test():
    print("第一步")
    yield 100
    print("第二步")
    yield 200
    print("第三步")
    yield 300

g=test()
print("生成器创建完成")
for x in g :
    print(x)

