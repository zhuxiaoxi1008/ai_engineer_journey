# -*- coding: utf-8 -*-
# 函数
# 学习日期: 2024-XX-XX

# 基本函数定义
def greet(name):
    """问候函数"""
    return f"你好, {name}!"

print(greet("Python"))

# 带默认参数的函数
def power(base, exponent=2):
    """计算幂次方"""
    return base ** exponent

print(f"3的平方: {power(3)}")
print(f"2的3次方: {power(2, 3)}")

# 可变参数函数
def sum_all(*numbers):
    """计算所有数字的和"""
    return sum(numbers)

print(f"1+2+3+4+5 = {sum_all(1, 2, 3, 4, 5)}")

# 关键字参数函数
def create_profile(**kwargs):
    """创建用户资料"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user_profile = create_profile(
    name="张三",
    age=25,
    city="北京"
)
print(f"用户资料: {user_profile}")

# Lambda函数
square = lambda x: x ** 2
print(f"5的平方: {square(5)}")

# 高阶函数示例
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"平方列表: {squared}")

# 过滤偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数列表: {evens}")
