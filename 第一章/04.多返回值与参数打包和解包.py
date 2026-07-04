# 多返回值
def cal(x,y):
    res1 = x + y
    res2 = y - x
    return res1, res2 # 如果不写返回值的形式的话，默认返回元组，即(res1,res2)

# 函数参数的打包与解包
# 1. 打包接收参数。
# *args的作用是打包所有位置参数，并形成元组。
# **kwargs的作用是打包所有关键字参数并形成字典
def foo(*args, **kwargs):
    print(args) # 元组
    print(kwargs) # 字典

# 2. 解包传递参数。
# *变量名: 作用是将参数（元组）解包为一个一个的独立的位置参数。
# **变量名: 作用是将参数（字典）解包为一个一个的key=value的关键字参数

nums = (10,20,30)
person = {'name':'john','age':18, 'gender':'male'}

foo(*nums, **person)