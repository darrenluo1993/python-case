from sys import path, argv

from fibo import fib2

print(fib2(500))
print("————————————————————————————————————————————————————————————————————")
print("--------------------------------------------------------------------")
for value in path:
    print(value)
print("————————————————————————————————————————————————————————————————————")
print("--------------------------------------------------------------------")
for arg in argv:
    print(arg)
