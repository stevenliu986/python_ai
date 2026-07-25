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
    6. yield from 能把一个“可迭代对象”里的东西依次 yield 出去。（替代 for + yield)
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

def demo(num_list):
    """num_list 这个参数为可迭代对象"""
    yield from num_list

nums = [10,20,30,40]

d = demo(nums)
for item in d:
    print(item)

# 使用生成器改写 Person 类
class Person:
    def __init__(self, name, age, gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 下面的代码实际上添加了一个快照，如果后续修改了其中任一值，这个迭代出来的还是旧值
        # self.__attrs = [name, age, gender,address]

    def __iter__(self):
        yield self.name
        yield self.age
        yield self.gender
        yield self.address
        # yield from self.__attrs 这种写法是不正确的，它违背了使用生成器和 __iter__ 的核心设计原则。

p1 = Person('John', 34, 'Male', 'Sydney')

for attr in p1:
    print(attr)

# 使用生成器编写函数生成斐波那契数
def fibonacci(n):
    pre = 1
    cur = 1

    for i in range(n):
        if i < 2:
            yield pre
        else:
            value = pre + cur
            pre = cur
            cur = value
            yield value

def optimised_fibonacci(n):
    """生成前 n 个斐波那契数: 0, 1, 1, 2, 3, 5, ..."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

f1 = fibonacci(15)
for item in f1:
    print(item)

# 无论是迭代器还是生成器对象，都可以用list,tuple,set等拿到其里面的所有内容（注意：容易挤爆内存）
fibo_list = list(optimised_fibonacci(15))
print(fibo_list)

# 生成器表达式：一种用类似列表推导式的语法，快速创建生成器对象的方法
# 语法：(表达式 for 变量 in 可迭代对象)
# 使用生成器表达式的场景：当“每个结果只依赖当前的这一个元素”时

nums1 = [10,20,30,40]

# 列表推导式
nums1_list = [n * 2 for n in nums1]

# 生成器表达式
gen1 = (n * 2 for n in nums1)
print(list(gen1))