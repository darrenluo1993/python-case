#!/usr/bin/python3

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append(40)
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
print("修改前ID：", id(mylist))
changeme(mylist)
print("修改后ID：", id(mylist))
print("函数外取值: ", mylist)
print(mylist[3])
print(mylist[4])
