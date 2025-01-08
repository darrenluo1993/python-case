#!/usr/bin/env python3

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_news = [name.upper() for name in names if len(name) > 3]
print(type(new_news))
print(new_news)

multiples = [i for i in range(30) if i % 3 == 0]
print(type(multiples))
print(multiples)
