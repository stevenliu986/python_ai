"""
初级:
    考察基本方法：append(), insert(), remove(), pop(), len(), index(),
    count(), sort(), reverse(), extend(), 切片, in 等基础用法。
"""

# 1. append 方法。给定列表 fruits = ['apple', 'banana', 'cherry']，在末尾添加 'orange'，打印结果。
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('orange')
# print(fruits)

# 2. insert 方法。给定列表 nums = [1, 2, 4, 5]，在索引 2 的位置插入 3，打印结果。
# nums = [1, 2, 4, 5]
# nums.insert(2,3) # 2 是索引位置，3 是插入元素
# print(nums)

# 3. remove 方法。给定列表 colors = ['red', 'green', 'blue', 'green']，删除第一个 'green'，打印结果。
# colors = ['red', 'green', 'blue', 'green']
# colors.remove('green')
# print(colors)

# 4. remove 方法。给定列表 stack = [10, 20, 30]，弹出最后一个元素并打印弹出的值和剩余列表。
# stack = [10, 20, 30]
# ele = stack.pop() # 如果没有传入参数（列表索引），则弹出列表末尾元素
# print(ele)
# print(stack)

# 5. index 方法。给定列表 letters = ['a', 'b', 'c', 'd', 'e']，查找 'c' 的索引，打印结果。
# letters = ['a', 'b', 'c', 'd', 'e','c']
# index = letters.index('c') # 查找第一个匹配的元素的索引
# print(index)

# 6. count 方法。给定列表 votes = ['yes', 'no', 'yes', 'yes', 'no', 'yes']，统计 'yes' 出现的次数。
# votes = ['yes', 'no', 'yes', 'yes', 'no', 'yes']
# count = votes.count('yes')
# print(count)

# 7. sort 方法。给定列表 scores = [88, 72, 95, 63, 78]，对其进行升序排序，打印结果。
# scores = [88, 72, 95, 63, 78]
# scores.sort()
# print(scores)

# 8. reverse 方法。给定列表 word = ['H', 'e', 'l', 'l', 'o']，反转列表，打印结果。
# word = ['H', 'e', 'l', 'l', 'o']
# word.reverse()
# print(word)

# 9. extend 方法。给定 list1 = [1, 2, 3] 和 list2 = [4, 5, 6]，将 list2 扩展到 list1 末尾，打印结果。
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2) # 与append 方法的整体合并不同，extend 方法是逐项合并
# print(list1)

# 10. in 方法。给定列表 animals = ['cat', 'dog', 'rabbit']，判断 'dog' 和 'fish' 是否在列表中，分别打印结果。
# animals = ['cat', 'dog', 'rabbit']
# print('dog' in animals)
# print('fish' in animals)
