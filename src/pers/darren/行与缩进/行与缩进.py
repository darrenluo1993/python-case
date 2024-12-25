# 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
#
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
#
# 实例(Python 3.0+)
if True:
    print("True")
else:
    print("False")
# 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
#
# 实例
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
# print ("False")    # 缩进不一致，会导致运行错误

# 以上程序由于缩进不一致，执行后会出现类似以下错误：
#
#  File "test.py", line 6
#     print ("False")    # 缩进不一致，会导致运行错误
#                                       ^
# IndentationError: unindent does not match any outer indentation level
