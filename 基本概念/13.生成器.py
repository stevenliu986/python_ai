"""
生成器：
    1. 生成器函数：函数体中如果出现了 yield 关键字，那函数是生成器函数
    2. 生成器对象：调用 “生成器函数” 时，该函数不会立即执行，而是返回一个生成器对象
    3. 写在“生成器函数”中的代码，需要通过“生成器对象”来执行
        a. 调用“生成器对象”中的 __next__ 方法，会让“生成器函数”的代码开始执行
        b. 当“生成器函数”的代码开始执行后，遇到 yield 会“暂停”执行，并且其内部会记录“暂停”的位置
        c. 后续调用 __next__ 方法时，会从上一次“暂停”的位置继续运行，直到再次遇到 yield
        d. 遇到 return 会抛出 StopIteration 异常，并将 return 后面的表达式作为异常信息
        e. yield 后面所写的表达式，会作为本次  __next__ 方法的返回值
    4. 生成器对象是一种特殊的迭代器
    5. yield 也能写在 for 循环里
    6. yield from 能把一个“可迭代对象”里的东西依次 yield 出去。（替代 for + yield）
    7. 生成器.send(值)可以让生成器继续执行的同时，给上一次 yield 传值
"""
def add(x,y):
    return x + y

def my_generator():
    print('step 1')
    yield add(1,10)
    print('step 2')
    yield 2
    print('step 3')
    yield 3
    return '结束了'

g = my_generator()
result = next(g)
print(result)
next(g)
next(g)
# next(g)
# print(next(g))
# print(next(g)) # 这是最后一步
# print(next(g)) # 这个会抛出 StopIteration 异常

def demo():
    nums = [10,20,30,40]
    yield from nums

d = demo()
for item in d:
    print(item)