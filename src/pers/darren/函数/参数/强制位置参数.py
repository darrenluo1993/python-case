#!/usr/bin/env python
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:

def func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


func(1, 2, 3, 4, e=5, f=6)
