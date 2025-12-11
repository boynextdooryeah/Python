#ToDo 题目：编写一个名为 @memoize 的函数装饰器，它能够缓存函数的调用结果
# 缓存(Cache)的含义：记住之前算过的结果，下次遇到一样的输入，直接返回记住的答案，不用再算一遍
# 。

def memoize(func):
    cache = {}  # 缓存字典：key -> result

    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))
#todo                             kwargs = {'x': 5, 'y': 3}
#                                 kwargs.items()   -→ dict_items([('x', 5), ('y', 3)])
#                          sorted让键值对按键名排序
#                            因为 add(a=1, b=2) 和 add(b=2, a=1) 应该被认为是同一个调用！
#                            如果不排序，前者变成 (('a',1),('b',2))，后者变成 (('b',2),('a',1))，两个 key 不同，缓存就失效了
#                     tuple()将列表(不可hash)转为元组(可hash) -> (('x',5),('y',3))
#             最后和args拼成一个大元组-??-

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result

        return result

    return wrapper


@memoize
def add(a, b, c=0):
    print(f"计算 {a} + {b} + {c}")
    return a + b + c


print(add(1,2))
print(add(1,2))
print(add(1,2,c=5))
print(add(1,2,c=5))

