#todo 迭代器只能往前不会后退,是访问集合元素的一种方式,是一个可以记住遍历的位置的对象
#      有两个基本的方法：iter() 和 next()
#      iterator n.迭代器,迭代程序   str, list, tuple都可用于创建迭代器 --iterate,iteration

list1 = [0,1,2,3,4]
it = iter(list1)
print(next(it))
print(next(it))
for x in it:
    print(x,end=' ')
print('\n',end='')

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

my_class = MyNumbers()
my_iter = iter(my_class)
for i in range(5):
    print(next(my_iter))

#todo 使用了 yield 的函数被称为生成器（generator）
#     生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
#     生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。

def countdown(n):
    while n > 0:
        yield n
        n -= 1
# 创建生成器对象
generator = countdown(5)
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
# 使用 for 循环迭代生成器
for value in generator:
    print(value)        # 输出: 2 1

import sys
# 生成器函数 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

# f 是一个迭代器，由生成器返回生成
f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
