#!/usr/bin/env python3

str_list = ["1", "2", "3", "3"]
str_set = {str + "!" for str in str_list if str != "3"}
print(type(str_set))
print(str_set)
