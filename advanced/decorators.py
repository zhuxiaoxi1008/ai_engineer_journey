# -*- coding: utf-8 -*-
# 装饰器
# 学习日期: 2024-XX-XX

import time
from functools import wraps

# 基本装饰器
def my_decorator(func):
    """简单装饰器"""
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("你好！")

say_hello()

# 带参数的装饰器
def repeat(times):
    """重复执行函数"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"你好, {name}!")

greet("Python")

# 计时装饰器
def timer(func):
    """计算函数执行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("执行完成")

slow_function()

# 缓存装饰器
def memoize(func):
    """缓存函数结果"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"斐波那契数列第10项: {fibonacci(10)}")
