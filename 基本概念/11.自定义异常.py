# 当程序遇到不符合预期的情况下，可以使用 raise 手动抛出异常
try:
    age = int(input('请输入你的年龄：'))
    if 18 <= age <= 120:
        print('成年')
    elif 0 <= age < 18:
        print('未成年')
    else:
        raise ValueError('年龄应为0 ~ 120的整数') # 在这里手动抛出异常
except Exception as err:
    print(f'异常信息是：{err}')

# 异常的传递链条
def test1():
    print('*******test1开始*******')
    result = 100 + '100'
    print('*******test1结束*******')

def test2():
    print('*******test2开始*******')
    test1()
    print('*******test2结束*******')

def test3():
    print('*******test3开始*******')
    test2()
    print('*******test3结束*******')

# 由于 test1 的异常没有处理，所以会沿着调用链进行传递，最终会传递给 test3。
# 所以可以在其中的任命一个环节进行异常处理，但越早处理越好。下面的是在test3进行处理
try:
    test3()
except Exception as e:
    print(e)

"""
自定义异常
    1. 可以继承 Exception 这个异常父类
"""

# 这是一个简单的自定义异常类
class SchoolNameError(Exception):
    def __init__(self,msg):
        super().__init__('校名异常' + msg)

raise SchoolNameError('学校名称过长')