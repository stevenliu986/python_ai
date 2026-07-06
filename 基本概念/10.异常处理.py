"""
为什么要进行异常处理：
    1. 程序运行过程中出现的异常，如果得不到处理，程序就会立即崩溃，导致后面的代码无法运行
    2. 异常处理不是让异常消失，而是将异常捕获到，随后根据异常的具体情况，来执行指定的逻辑
"""

# 未进行异常处理，在两个输入的语句和计算语句有可能会出现异常
# print('欢迎使用本程序')
# a = int(input('请输入第1个数：'))
# b = int(input('请输入第2个数：'))
# result = a/b
# print(f'{a}和{b}的计算结果是{result}')

"""
异常处理：
    1. 将可能出现异常的代码放在 try 中，出现异常后处理的代码放在 except 中
    2. 如果 try 中的代码出现异常，那 try 中的后续代码将不会执行，并自动跳到 except 中进行处理
    3. 如果 try 中的代码没有异常，那 except 中的代码就不会执行
    4. 无论是否发生异常，try-except 后面的代码都会继续执行
    5. 可以指定特定的异常来使异常处理更有目的性。
    6. except 可以写多个，不受限制。只要匹配上，后续的 except 就不会处理了。所以 except 要按照从窄到宽的原则
    7. BaseException 是所有异常的父类，Exception 是常见异常的父类
"""
# try:
#     print('欢迎使用本程序')
#     c = int(input('请输入第1个数：'))
#     d = int(input('请输入第2个数：'))
#     print(x) # 会触发异常，但会在最后兜底的异常语句被捕获到
#     result = c / d
#     print(f'{c}和{d}的计算结果是{result}')
# except ZeroDivisionError:
#     print('除数不能是0')
# except ValueError:
#     print('请输入数字')
# except Exception as e: # 对异常处理进行兜底
#     print(f'捕获到的异常信息是{e}')
#     print(f'捕获到的异常类型是{type(e)}')
#     print(f'捕获到的异常参数是{e.args}')
# print('这是后续执行的逻辑1')
# print('这是后续执行的逻辑2')

# 验证异常之间的继承关系
print(issubclass(ZeroDivisionError, ArithmeticError)) # True
print(issubclass(ZeroDivisionError, Exception)) # True
print(issubclass(ArithmeticError, Exception)) # True

# 上面的异常处理还可以修改为下面的代码
try:
    print('欢迎使用本程序')
    c = int(input('请输入第1个数：'))
    d = int(input('请输入第2个数：'))
    # print(x) # 会触发异常，但会在最后兜底的异常语句被捕获到
    result = c / d
    print(f'{c}和{d}的计算结果是{result}')
except (ZeroDivisionError, ValueError, Exception) as e:
    if isinstance(e, ZeroDivisionError):
        print('除数不能是0')
    elif isinstance(e, ValueError):
        print('请输入数字')
    else:
        print(f'捕获到的异常信息是{e}')
        print(f'捕获到的异常类型是{type(e)}')
        print(f'捕获到的异常参数是{e.args}')
print('这是后续执行的逻辑1')
print('这是后续执行的逻辑2')

"""
异常处理的完整写法：
    1. try:     尝试做可能会出现异常的事情
    2. except:  出在异常时处理
    3. else:    如果没有出现异常要做的事情
    4. finally: 无论有没有异常都要做的事情
"""
