"""
装饰器
1. 装饰器是一种"可调用对象"（通常是函数），它能接收一个函数作为参数，并且会返回一个新函数
2. 装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能

关键点：
    1. 接收被装饰的函数，同时返回新函数（wrapper）
    2. 装饰器"吐出来"的是 wrapper 函数，以后别个调用的也是 wrapper 函数
    3. 为了保证参数的兼容性，wrapper 函数要通过 *args，**kwargs 接收参数
    4. wrapper 函数主要做的是：调用原函数（被装饰的函数），执行其他逻辑，但要记得将原函数的返回值返回出去
"""
from functools import wraps # 一定要使用 @wraps(func)，否则会丢失原函数的 __name__、__doc__ 等信息。

# 这就是装饰器函数
def say_hello(func):
    def wrapper(*args,**kwargs):
        print('你好，我要开始计算了。。。')
        return func(*args,**kwargs)
    return wrapper

@say_hello
def add(x,y):
    res = x + y
    print(f'{x}和{y}相加的值是{res}')
    return res

# 这是经过装饰的 add 函数，既可以使用位置参数的形式传参，也可以使用关键字参数的形式传参
result = add(y=10,x=20)

# 进阶：可接收参数的装饰器
def say_hello1(msg):
    def decorator(func):
        @wraps(func) # 一定要使用 @wraps(func)，否则会丢失原函数的 __name__、__doc__ 等信息
        def wrapper(*args, **kwargs):
            print(f'你好，我要开始{msg}计算了。。。')
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 添加可接收参数的装饰器
@say_hello1('减法')
def sub(x,y):
    return x - y

result01 = sub(40,20)
print(result01)

"""
类装饰器：“用类实现的函数装饰器”，注意，它是用于函数的，而不是用于类的，用于类的装饰器称为“装饰类的装饰器”，也是用函数的形式来声明的
    1. 包含 __call__ 方法的类，就是类装饰器
    2. 像调用函数一样去调用类装饰器的实例对象，就会触发 __call__ 方法的调用
    3. __call__ 方法通常接收一个函数作为参数，并且会返回一个新的函数
"""

class SayHello01:

    def __call__(self,func):
        def wrapper(*args, **kwargs):
            print(f'我要开始{self.msg}计算了。。。')
            return func(*args, **kwargs)
        return wrapper

class SayHello02:
    # 如果这个类装饰器编写了 __init__ 函数，则表明这个类装饰器是可以接收参数的
    def __init__(self,msg):
        self.msg = msg

    def __call__(self,func):
        def wrapper(*args, **kwargs):
            print(f'我要开始{self.msg}计算了。。。')
            return func(*args, **kwargs)
        return wrapper

@SayHello01() # 对于类装饰器，必须要带()
def add01(x,y):
    return x + y