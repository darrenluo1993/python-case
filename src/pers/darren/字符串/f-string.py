name = 'Runoob'

print('Hello %s' % name)

print(f'Hello {name}')  # 替换变量

print(f'{1 + 2}')  # 使用表达式

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

# 在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：
x = 1
print(f'{x + 1=}')  # Python 3.8
