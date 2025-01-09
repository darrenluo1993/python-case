#!/usr/bin/python3

# 可写函数说明
def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    if vartuple:
        print(vartuple)
        print(vartuple[0])


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)
printinfo(80, (50, 60), (1, 2))

print("---------------------------")


def printinfo2(arg1, **vartuple):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    if vartuple:
        print(vartuple)
        print("vartuple['a']:", vartuple['a'])


# 调用printinfo2 函数
printinfo2(10)
printinfo2(70, a=60, b=50)
printinfo2(80, a=(50, 60), b=(1, 2))

print("---------------------------")


def printinfo3(arg1, arg2, *vartuple, arg4):
    print(arg1 + arg2 + arg4)
    print(arg1 + arg2 + vartuple[0] + vartuple[1] + arg4)


printinfo3(1, 2, 4, 5, arg4=3)
printinfo3(1, 2, 4, 5, 6)  # 报错：missing 1 required keyword-only argument: 'arg4'
