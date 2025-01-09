#!/usr/bin/env python

def before_call_code():
    print("Before calling the target function")


def after_call_code():
    print("After calling the target function")


def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()
        result = original_function(*args, **kwargs)
        # 这里是在调用原始函数后添加的新功能
        after_call_code()
        return result

    return wrapper


# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    print("Target function called with arguments:", arg1, arg2)


target_function("Hello", "World")
