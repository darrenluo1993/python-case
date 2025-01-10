#!/usr/bin/env python3

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_news = [name.upper() for name in names if len(name) > 3]
print(type(new_news))
print(new_news)

multiples = [i for i in range(30) if i % 3 == 0]
print(type(multiples))
print(multiples)

print('----------------------')
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
list1 = [x * y for x in vec1 for y in vec2]
print(list1)  # [8, 6, -18, 16, 12, -36, 24, 18, -54]
list2 = [x + y for x in vec1 for y in vec2]
print(list2)  # [6, 5, -7, 8, 7, -5, 10, 9, -3]
list3 = [vec1[i] * vec2[i] for i in range(len(vec1))]
print(list3)  # [8, 12, -54]
