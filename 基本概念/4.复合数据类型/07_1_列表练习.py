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

# 4. pop 方法。给定列表 stack = [10, 20, 30]，弹出最后一个元素并打印弹出的值和剩余列表。
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

"""
中级:
    考察列表方法组合使用、切片高级用法、列表推导式基础、嵌套列表操作、copy() 等。
"""

# 1. 给定列表 data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]，去除重复元素并保持原始顺序，打印结果。
# data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 传统循环方式（兼容性最强） - 保持原列表元素顺序不变
# unique = []
# for num in data:
#     if num not in unique:
#         unique.append(num)
#
# print(unique)

# 使用 Python 3.7+ 的 dict.fromkeys
# dict.fromkeys() 会将 data 中的值作为 key 生成一个字典，由于未传 value 所以是这样的形式 {key1: None,
# key2: None, ..., keyn: None}
# unique1 = list(dict.fromkeys(data))
# print(unique1)

# 2. 列表浅拷贝 vs 深拷贝。打印 a 和 b，解释为什么 a 也变了。然后用 copy.deepcopy 实现真正的深拷贝。
# a = [[1, 2], [3, 4]]
# b = a.copy()
# b[0][0] = 99
# print(a)
# print(b)

# import copy
# c = copy.deepcopy(a)
# c[0][0] = 99
# print(c)

# 3. 交替合并。给定 list1 = [1, 3, 5, 7] 和 list2 = [2, 4, 6, 8]，交替合并为 [1, 2, 3, 4, 5, 6, 7, 8]。
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]

# 下面的方法仅对长度相同的列表有效
# result = [x for pair in zip(list1, list2) for x in pair]
# print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]

# 使用传统的循环方法 - 可兼容长度不相同的列表进行合并
# merged_list = [] # 声明合并列表
# max_len = max(len(list1), len(list2)) # 取长度大的列表的长度
# for i in range(max_len):
#     if i < len(list1):
#         merged_list.append(list1[i])
#     if i < len(list2):
#         merged_list.append(list2[i])
#
# print(merged_list)

# 4. 给定列表 nums = [1, 2, 3, 2, 4, 2, 5]，删除所有值为 2 的元素（不能用列表推导式，用循环 + remove 实现）。
# nums = [1, 2, 3, 2, 4, 2, 5]
#
# for item in nums:
#     if item == 2:
#         nums.remove(item)
#
# print(nums)

# 5. 列表切片赋值。给定 lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，用切片赋值将索引 2 到 5（不含 5）的元素替换为 [20, 30]，打印结果。
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst[2:5] = [20,30]
# print(lst)

# 6. 给定 temperatures = [23, 45, 12, 67, 34, 89, 5]，分别找出最大值和最小值的索引。
temperatures = [23, 45, 12, 67, 34, 89, 5]

# 方法一：需要循环 4 次
max_temperature1 = max(temperatures)
min_temperature1 = min(temperatures)
max_index1 = temperatures.index(max_temperature1)
min_index1 = temperatures.index(min_temperature1)
print(max_index1)
print(min_index1)

# 方法二：使用enumerate 方法
max_temperature2 = min_temperature2 = temperatures[0]
max_index2 = min_index2 = 0
for i, temperature in enumerate(temperatures):
    if temperature > max_temperature2:
        max_temperature2 = temperature
        max_index2 = i
    if temperature < min_temperature2:
        min_temperature2 = temperature
        min_index2 = i

# 这段代码是使用 java 的思维来解决问题，在 python 中不推荐
# for i in range(len(temperatures)):
#     if temperatures[i] > max_temperature2:
#         max_temperature2=temperatures[i]
#         max_index2 = i
#     if temperatures[i] < min_temperature2:
#         min_temperature2=temperatures[i]
#         min_index2 = i

print(f'最大值的索引为：{max_index2}')
print(f'最小值的索引为：{min_index2}')

# 方法三：
max_index3 = max(range(len(temperatures)), key=lambda index: temperatures[index])
min_index3 = min(range(len(temperatures)), key=lambda index: temperatures[index])

print(f'最大值的索引为：{max_index3}')
print(f'最小值的索引为：{min_index3}')

# 7. 给定列表 items = list(range(1, 11))，将其按每 3 个一组分块，得到 [[1,2,3], [4,5,6], [7,8,9], [10]]。
items = list(range(1,11))
def foo(lst,*,step = 1):
    temp = [lst[i:i+step] for i in range(0,len(lst),step)]
    return temp

print(foo(items, step=3))

# 8. 给定 words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']，用字典统计每个元素出现的频率。
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
dict1 = {}
for word in words:
    dict1[word] = dict1.get(word, 0) + 1
print(dict1)

# 9. 给定列表 arr = [1, 2, 3, 4, 5]，向右旋转 2 个位置，得到 [4, 5, 1, 2, 3]。
arr = [1, 2, 3, 4, 5]
new_arr = arr[3:] + arr[:3]
print(new_arr)

# 10. 给定 matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]，用列表推导式提取所有元素为扁平列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]。
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in matrix for item in sublist]
print(flat_list)

# 11. 给定 a = [1, 2, 3, 4, 5] 和 b = [4, 5, 6, 7, 8]，分别求它们的交集和并集（用列表实现，不用 set）。
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
common_list = [item for item in a if item in b]
print(common_list)

union_list = a + [x for x in b if x not in a]
print(union_list)

# 12. 给定 nums = list(range(1, 21))，筛选出所有偶数并求它们的平方，存入新列表。
nums = list(range(1, 21))
new_list = [item**2 for item in nums if item % 2 == 0]
print(new_list)

# 13. 给定 nums = [-5, 3, -1, 4, -2, 7]，按绝对值从小到大排序，打印结果。
nums1 = [-5, 3, -1, 4, -2, 7]
result = sorted(nums1, key=abs)
print(result)

# 14. 给定 names = ['Alice', 'Bob', 'Charlie'] 和 ages = [25, 30, 35]，用 zip 将它们组合成 [('Alice', 25), ('Bob', 30), ('Charlie', 35)]。
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
lst01 = list(zip(names, ages))
print(lst01)

# 15. 实现函数 rotate_left(lst, k)，将列表循环左移 k 个位置。例如 [1,2,3,4,5] 左移 2 位得到 [3,4,5,1,2]。
def rotate_left(lst, k):
    return lst[k:] + lst[:k]
lst02 = [1,2,3,4,5]
lst03 = rotate_left(lst02, 2)
print(lst03)

# 16. 给定 lst = [1, 1, 2, 2, 2, 3, 4, 4, 5]，删除连续重复元素，得到 [1, 2, 3, 4, 5]。
lst04 = [1, 1, 2, 2, 2, 3, 4, 4, 5]
unique01 = []
for num in lst04:
    if num not in unique01:
        unique01.append(num)
print(unique01)

# 17. 不用 sort()，手动实现插入排序对列表 [64, 34, 25, 12, 22, 11, 90] 进行排序。
def insert_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

lst05 = [64, 34, 25, 12, 22, 11, 90]
insert_sort(lst05)
print(lst05)

def buble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
lst06 = [12,5,2,3,9]
buble_sort(lst06)
print(lst06)

# 18. 给定 scores = [10, 8, 10, 6, 7, 9, 5]，找出第二大的元素（考虑重复）。
scores = [10, 8, 10, 6, 7, 9, 5]
second_largest = sorted(set(scores))[-2]
print(second_largest)

# 方法二 - 基础 for 循环实现
first_largest = float('-inf') # 先设置为无穷小
second_largest = float('-inf') # 先设置为无穷小
for score in scores:
    if score > first_largest:
        second_largest = first_largest
        first_largest = score
    elif score > second_largest and score != first_largest:
        second_largest = score

print(second_largest)

# 19. 给定 students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'B'), ('Eve', 'A')]，
# 按等级分组为字典 {'A': [...], 'B': [...]}。
students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'B'), ('Eve', 'A')]
# from collections import defaultdict
#
# grouped = defaultdict(list)
# for name, grade in students:
#     grouped[grade].append(name)
#
# print(dict(grouped))

lstA = []
lstB = []
for name,grade in students:
    if grade == 'A':
        lstA.append(name)
    else:
        lstB.append(name)
grouped = {'A': lstA, 'B': lstB}
print(grouped)

# 20 不用内置 map 和 filter，用列表推导式实现：
# 将 [1, 2, 3, 4, 5] 每个元素乘以 2
# 筛选出大于 5 的元素
lst07 = [item*2 for item in [1, 2, 3, 4, 5]]
lst08 = [item for item in lst07 if item > 5]
print(lst07)
print(lst08)

"""
高级练习题：
    考察递归、生成器与列表配合、复杂嵌套操作、算法思维、性能优化、函数式编程等。
"""

# 1. 给定 nums = [1, 2, 3]，生成所有全排列（不使用 itertools）。
def permute_in_place(nums):
    res = []
    n = len(nums)

    def backtrack(first=0):
        # 填满了所有位置
        if first == n:
            res.append(nums[:])  # 保存当前 nums 的一份副本
            return

        for i in range(first, n):
            # 动态维护数组：把第 i 个元素换到第 first 个位置
            nums[first], nums[i] = nums[i], nums[first]
            # 递归填下一个位置
            backtrack(first + 1)
            # 撤销交换（回溯）
            nums[first], nums[i] = nums[i], nums[first]

    backtrack()
    return res

print(permute_in_place([1, 2, 3]))
