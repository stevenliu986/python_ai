# map 函数：对一组数据中的每一个元素统一执行某种操作并生成一种新数据。
# 语法：map(操作函数，可迭代对象)

nums = [10,20,30,40]
def double(x):
    return x*2

# map 函数返回的是一个迭代器对象，需要手动迭代或进行类型转换
result = map(lambda x: x * 2, nums)
result1 = list(result)
print(result1)

for item in result1:
    print(item)

result2 = [x * 2 for x in nums]
print(result2)

str_tuple = ('python', 'java', 'js')
result3 = (x.upper() for x in str_tuple)
print(tuple(result3))

# filter 函数：从一组数据中筛选出符合条件的元素并组成新数据
# 语法：filter(过滤函数，可迭代对象)
result4 = list(filter(lambda x: x > 20, nums))
print(result4)

result5 = [x for x in nums if x > 20]
print(result5)

# sorted 函数：对一组数据进行排序，返回一组新数据
# 语法：filter(可迭代对象,key=xxx,reverse=xxx)

# 数字排序
nums1 = [50,10,30,20,11]
result6 = sorted(nums1, reverse=True) # 添加 reverse 表示要从大到小进行排序
print(result6)

# 字符串排序
languages = ['java', 'sql', 'python','js']
# 根据字符串的长度排序
result7 = sorted(languages, key=lambda s: len(s)) # 这里的key就是筛选的依据
print(result7)

# 还可以这样改写
result8 = sorted(languages,key=len)
print(result8)

# reduce 函数。使用它需要从functools模块导入
from functools import reduce

result9 = reduce(lambda m,n: m + n, nums1)
print(result9)
