# -*- coding: utf-8 -*-
# 控制流
# 学习日期: 2024-XX-XX

# if-else 语句
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"分数: {score}, 等级: {grade}")

# for 循环
print("\nfor循环示例:")
for i in range(5):
    print(f"数字: {i}")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("\n水果列表:")
for fruit in fruits:
    print(f"- {fruit}")

# while 循环
print("\nwhile循环示例:")
count = 0
while count < 3:
    print(f"计数: {count}")
    count += 1

# break 和 continue
print("\nbreak和continue示例:")
for i in range(5):
    if i == 2:
        continue  # 跳过2
    if i == 4:
        break     # 在4处停止
    print(f"处理数字: {i}")
