"""
列表推导式：用一条简洁语句，从可迭代对象中生成新列表的语法结构
备注：列表推导式本质是对 for 循环 + append() 的一种简写形式
语法格式：[表达式 for 变量 in 可迭代对象]
"""

# 需求：求列表中的元素两倍
# 方法一：使用map方法
nums = [10,20,30,40]
result01= list(map(lambda n:n*2, nums))
print(result01)

# 方法二：使用 for + append
result02 = []
for item in nums:
    result02.append(item * 2)

print(result02)

# 方法三：列表推导式
result03 = [n * 2 for n in nums]
print(result03)

# 需求：只计算列表中元素值大于20的
result04 = [n *2 for n in nums if n>20]
print(result04)

# 字典推导式
names = ['John', 'Tom', 'Jerry']
ages = [12,11,23]
result05 = {names[i]:ages[i] for i in range(len(names))}
print(result05)

