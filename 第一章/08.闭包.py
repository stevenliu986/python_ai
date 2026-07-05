def outer():
    num = 10
    def inner():
        # 如果要修改外部函数中的变量，需要使用nonlocal
        nonlocal num
        num += 1
        print(num)

    return inner

f = outer()
f() # 11
f() # 12
f() # 13

"""
1. out函数中，被inner函数中所使用到的那些变量，会被封存到 闭包单元cell 中 
2. 这些 cell 会组成一个 __closure__ 元组，最终放在 inner 函数上
"""

# 打印 __closure__ 元组
print(f.__closure__)

# 打印 __closure__ 元组的某一项
print(f.__closure__[0])

# 打印 __closure__ 元组的某一项的具体值
print(f.__closure__[0].cell_contents)