# -*- coding: utf-8 -*-
# 继承与多态
# 学习日期: 2024-XX-XX

# 基类
class Animal:
    """动物基类"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """发出声音"""
        raise NotImplementedError("子类必须实现speak方法")
    
    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}"

# 子类1
class Dog(Animal):
    """狗类"""
    
    def speak(self):
        return f"{self.name}汪汪叫！"

# 子类2
class Cat(Animal):
    """猫类"""
    
    def speak(self):
        return f"{self.name}喵喵叫！"

# 多态示例
def animal_sound(animal):
    """让动物发出声音"""
    print(animal.speak())

# 创建对象
dog = Dog("旺财")
cat = Cat("咪咪")

# 多态调用
animal_sound(dog)
animal_sound(cat)

# 多重继承示例
class Flyable:
    """可飞行"""
    def fly(self):
        return "我能飞！"

class Swimmable:
    """可游泳"""
    def swim(self):
        return "我能游泳！"

class Duck(Animal, Flyable, Swimmable):
    """鸭子类 - 多重继承"""
    
    def speak(self):
        return f"{self.name}嘎嘎叫！"

# 创建鸭子对象
duck = Duck("唐老鸭")
print(duck.introduce())
print(duck.speak())
print(duck.fly())
print(duck.swim())
