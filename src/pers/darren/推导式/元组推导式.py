# ！/usr/bin/python3

tup = ("baidu", "google", "bing")
new_tup = (val.upper() for val in tup if val != "baidu")
print(type(new_tup))
print(new_tup)
new_tup2 = tuple(new_tup)
print(type(new_tup2))
print(new_tup2)

a = (x ** 2 for x in range(1, 10, 2))
print(tuple(a))
