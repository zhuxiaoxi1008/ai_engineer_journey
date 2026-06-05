# -*- coding: utf-8 -*-
# 类与对象
# 学习日期: 2024-XX-XX

# 定义类
class Dog:
    """狗类"""
    
    # 类属性
    species = "犬科"
    
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name  # 实例属性
        self.age = age
    
    def bark(self):
        """吠叫方法"""
        return f"{self.name}汪汪叫！"
    
    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}，今年{self.age}岁"

# 创建对象
dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 2)

# 访问属性和方法
print(dog1.introduce())
print(dog1.bark())
print(f"{dog2.name}属于{dog2.species}")

# 修改属性
dog1.age = 4
print(f"{dog1.name}现在{dog1.age}岁了")

# 类方法示例
class Circle:
    """圆类"""
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """计算面积"""
        return self.pi * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        """从直径创建圆"""
        radius = diameter / 2
        return cls(radius)

# 使用类方法
circle = Circle.from_diameter(10)
print(f"圆的面积: {circle.area():.2f}")
