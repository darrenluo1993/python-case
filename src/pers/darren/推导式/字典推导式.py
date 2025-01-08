#!/usr/bin/env python3

listdemo = ['Google', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key: len(key) for key in listdemo}
print(type(newdict))
print(newdict)

dic = {x: x ** 2 for x in range(1, 10, 2)}
print(type(dic))
print(dic)
