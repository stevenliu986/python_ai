import os

path = 'a/b/c/d'

# os.mkdir(path)：创建单级目录，如果目录存在，则抛出异常
# os.mkdir('a')

# os.makedirs(path)：创建多级目录，如果所有的目录都存在，则抛出异常
# os.makedirs(path)

# os.rmdir(path)：删除空目录，如果目录非空或不存在，则抛出异常
# os.rmdir('a')
# os.rmdir('b')

# os.removedirs(path)：递归删除删除空目录。在成功删除末尾一级目录后，会向上尝试删除父级目录(直到父级目录不是空目录为止)
# os.removedirs('b/c/d/e')

# os.path.exists(path)：判断路径是否存在(目录/文件都算)，该方法会返回布尔值
# os.path.isdir(path)：用于判断路径，规则如下：
#   1. 路径不存在 -> False
#   2. 路径存在，但指向的是文件 -> False
#   3. 路径存在，且是目录 -> True

# result = os.path.isdir(path)
# print(result) # false

# os.path.isfile(path)：判断是否为文件
# result = os.path.isfile(path)
# print(result)

# os.scandir(path)：扫描指定目录
# result = os.scandir('a/b/c') # 返回的是一个迭代器
# for item in result:
#     print('目录' if item.is_dir() else '文件', item.name) # 三元表达式

# os.walk(path)：按层级递归遍历指定目录下所有子目录和文件
# result = os.walk('a')
# for item in result:
#     print(item)

# 练习2：日志记录。
#   1.用户输入用户名和密码后，程序进行校验：
#   2.用户名不存在，提示“用户名未注册”，并记录日志。
#   3.用户名存在，但密码错误，提示“密码错误”，并记录日志。
#   4.用户名和密码均正确，提示“登录成功”，并记录日志。

users = {
    'John':'123456',
    'Tom': '888888',
    'Jerry': 'abc123'
}

username = input('请输入用户名：')
password = input('请输入密码：')

if username not in users:
    print(f'该{username}未注册')
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{username} 用户未注册 \n')
elif users[username] != password:
    print('密码不正确')
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{username} 用户密码错误 \n')

else:
    print('登录成功')
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{username} 用户登录成功')