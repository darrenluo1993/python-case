#!/usr/bin/env python

def change(a):
    print(id(a))
    a = 10
    print(id(a))


a = 5
print(id(a))
change(a)
