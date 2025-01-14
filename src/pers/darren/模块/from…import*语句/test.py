#!/usr/bin/python3

# from ... import * 可直接访问模块中的内容
from sys import *

for p in path:
    print(p)
print("---------------------------------------------------------------------------")

# import 模块名 访问模块中的内容需要模块名.函数名
import fibo

fibo.fib(1000)
print(fibo.fib2(1000))
print("---------------------------------------------------------------------------")

# import 模块名 as 别名 访问模块中的内容需要别名.函数名
import fibo as fib

fib.fib(1000)
print(fib.fib2(1000))
print("---------------------------------------------------------------------------")

# from 模块名 import 函数名 访问模块中的内容需要函数名
from fibo import fib, fib2

fib(1000)
print(fib2(1000))
