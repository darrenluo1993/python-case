import sys

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
for name in dir(sys):
    print(name)

print("----------------------------------------------------------")
print("----------------------------------------------------------")

for name in dir():
    print(name)
