# ！/usr/bin/python3

list = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list)

iter1 = iter(list)
print(next(iter1))
print(next(iter1))

iter2 = iter(list)
for val in iter2:
    if val != list[-1]:
        print(val, end=", ")
    else:
        print(val)
