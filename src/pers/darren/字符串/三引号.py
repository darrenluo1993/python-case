#!/usr/bin/python3

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

sql = """
select
    FIELD1,
    FIELD2,
    FIELD3
from
    TEST_TABLE
where
    FIELD4 = "test"
order by
    FIELD5 desc
"""
print(sql)
