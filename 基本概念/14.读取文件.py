# Python 中操作文件的流程
#  1. 创建 文件对象
#  2. 操作文件（读，写等）
#  3. 关闭文件

# 文件操作核心：open 函数，它可以打开/新建文件，且支持多种操作模式，返回文件对象

# 读取操作一：使用“文件对象”的 read 方法，读取文件中的内容
# read方法说明：
#  1. read(size)中的size可选参数
#         若不传递size，表示读取文件的所有内容（注意内存占用）
#         若传递size，表示读取文件中指定个数的字符，或指定大小的字节（针对二进制文件）
#  2. read会从上一次read的位置继续读取，若到达文件末尾继续读取，则返回空字符串
# 创建 文件对象
file1 = open(file='a.txt', mode='rt', encoding='utf-8')

# 操作文件（读）
result = file1.read()
print(result)
# 关闭文件
file1.close()

print(f'{"-" * 20}')

# 读取操作二：使用“文件对象”的 readline 方法，读取文件中的一行内容
# readline方法说明：
#  1. readline(size)中的size可选参数，注意：size 不是行数
#         若不传递size，表示读取文件当前行的所有内容（注意内存占用）
#         若传递size，表示读取当前行中最多能读取的字符数，或字节数（针对二进制文件）
#  2. readline会从上一次的位置继续读取，若到达文件末尾继续读取，则返回空字符串

# 创建 文件对象
file2 = open(file='a.txt', mode='rt', encoding='utf-8')
# 操作文件（读
# line1 = file2.readline()
# line2 = file2.readline()
# line3 = file2.readline()
# line4 = file2.readline()
# print(line1,end='')
# print(line2,end='')
# print(line3,end='')
# print(line4,end='')

# print(f'{"-" * 20}')

# 通过循环打印每一行
while True:
    line = file2.readline()
    if line == '':
        break
    print(line,end='') # 也可用 print(line.strip())来代替

# 关闭文件
file2.close()
print()
print(f'{"-" * 20}')

# 最佳实践：使用 with 上下文管理器结合 for 循环，逐行读取文件
with open(file='a.txt', mode='rt', encoding='utf-8') as file:
    for line in file:
        print(line,end='')