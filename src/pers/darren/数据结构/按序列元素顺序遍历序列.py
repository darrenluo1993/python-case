#!/usr/bin/python3

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print("不去重遍历")
for f in sorted(basket):
    print(f)
print("去重遍历")
for f in sorted(set(basket)):
    print(f)
