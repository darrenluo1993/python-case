#!/usr/bin/env python3

# 强制关键字参数，参数d必须传关键字参数
def func(a, b, c, *, d, e):
    print(a, b, c, d, e)


func(1, 2, 3, d=4, e=5)
