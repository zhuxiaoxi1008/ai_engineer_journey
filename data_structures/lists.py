# -*- coding: utf-8 -*-
# 列表操作
# 学习日期: 2024-XX-XX

# 创建列表
fruits = ["苹果", "香蕉", "橙子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Python", 3.14, True]

# 访问元素
print(f"第一个水果: {fruits[0]}")
print(f"最后一个数字: {numbers[-1]}")

# 列表切片
print(f"前3个数字: {numbers[:3]}")
print(f"后2个数字: {numbers[-2:]}")

# 添加元素
fruits.append("葡萄")
fruits.insert(1, "草莓")
print(f"更新后的水果列表: {fruits}")

# 删除元素
fruits.remove("香蕉")
removed = fruits.pop()
print(f"移除后: {fruits}, 被移除的: {removed}")

# 列表推导式
squares = [x ** 2 for x in range(6)]
print(f"平方列表: {squares}")

# 列表方法
numbers.sort(reverse=True)
print(f"降序排列: {numbers}")

numbers.extend([6, 7, 8])
print(f"扩展后: {numbers}")

# 列表操作
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"合并列表: {combined}")

# 列表长度和元素存在性
print(f"列表长度: {len(fruits)}")
print(f"'苹果'在列表中: {'苹果' in fruits}")
