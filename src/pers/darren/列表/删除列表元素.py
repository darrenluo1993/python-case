#!/usr/bin/python3

list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)
list.remove('Runoob')
print("使用 remove() 删除的元素 : ", list)
