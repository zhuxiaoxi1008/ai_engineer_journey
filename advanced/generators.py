# -*- coding: utf-8 -*-
# 生成器
# 学习日期: 2024-XX-XX

# 生成器函数
def count_down(n):
    """倒计时生成器"""
    while n > 0:
        yield n
        n -= 1

# 使用生成器
print("倒计时:")
for num in count_down(5):
    print(num)

# 生成器表达式
squares = (x**2 for x in range(10))
print("\n平方数生成器:")
for i, sq in enumerate(squares):
    if i > 5:  # 只打印前6个
        break
    print(sq)

# 无限序列生成器
def fibonacci():
    """斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用无限生成器
print("\n斐波那契数列前10项:")
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()

# 批量读取文件的生成器
def read_in_chunks(file_path, chunk_size=1024):
    """分块读取文件"""
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# 管道生成器
def pipeline(data):
    """数据处理管道"""
    # 过滤偶数
    data = (x for x in data if x % 2 == 0)
    # 计算平方
    data = (x**2 for x in data)
    # 只保留小于50的
    data = (x for x in data if x < 50)
    return data

numbers = range(20)
print("\n管道处理结果:")
for result in pipeline(numbers):
    print(result, end=" ")
print()

# 生成器链
def numbers():
    for i in range(10):
        yield i

def squares(nums):
    for num in nums:
        yield num ** 2

def take(n, iterable):
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item

print("\n生成器链:")
for num in take(5, squares(numbers())):
    print(num, end=" ")
print()
