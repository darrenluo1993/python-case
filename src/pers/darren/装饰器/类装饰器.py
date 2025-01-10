class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前/之后执行的代码
        print("函数调用之前")
        result = self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        print("函数调用之后")
        return result


@DecoratorClass
def my_function(arg1, arg2):
    print("Hello, World!")
    print(arg1, arg2)
    return arg1 * arg2


print(my_function(2, 3))
