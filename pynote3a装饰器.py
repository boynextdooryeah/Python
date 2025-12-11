#TODO 装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数
# 使用 @decorator_name 来应用在函数或方法上 (Python 还提供了一些内置的装饰器)
# Python 装饰允许在 |不修改原有函数代码| 的基础上，动态地 |增加或修改函数| 的功能
# 本质上是一个  |接收函数作为输入|  并返回一个  |新的包装过后的函数|  的 |对象|
# 。

#ToDo                               函数装饰器
#todo 函数里定义函数，其实是代码块，调用外层函数时执行代码块，代码块是定义，所以定义了内部函数
def decorator_func(func):
    def wrapper(*args,**kwargs):
        print("before")
        func()
        print("after")
    return wrapper

@decorator_func
def say_motherfucker():
    print('hello motherfucker')

say_motherfucker()

#todo repeat 是一个通用装饰器——它不仅要能装饰无参函数，还要能装饰带任意参数的函数-->如greet(name)
# wrapper(*args,**kwargs)
# *args：接收所有位置参数（打包成元组）
# **kwargs：接收所有关键字参数（打包成字典）
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

#ToDo                              类装饰器






