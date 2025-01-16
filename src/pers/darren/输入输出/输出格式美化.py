s = "Hello World!"
print(str(s))
print(repr(s))

print(1 / 7)
print(str(1 / 7))

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)

#  repr() 函数可以转义字符串中的特殊字符
hello = 'Hello, World!\n'
print(hello)
print(repr(hello))

# repr() 的参数可以是 Python 的任何对象
tup = (x, y, ('Google\n', 'Runoob\t'))
print(tup)
print(tup[2][0])
print(repr(tup))
print(repr(tup[2][0]))

print("---------------------------------")
for x in range(1, 11):
    print(repr(x).rjust(2), end=' ')
    print(repr(x ** 2).rjust(3), end=' ')
    print(repr(x ** 3).rjust(4), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x ** 4).rjust(5))

print("---------------------------------")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x ** 2).rjust(3), repr(x ** 3).rjust(4), repr(x ** 4).rjust(5))

print("---------------------------------")
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d} {3:5d}'.format(x, x ** 2, x ** 3, x ** 4))

print("---------------------------------")
# zfill(), 它会在数字的左边填充 0
print("12".zfill(5))
