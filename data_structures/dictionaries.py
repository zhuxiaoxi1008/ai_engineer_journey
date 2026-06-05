# -*- coding: utf-8 -*-
# 字典操作
# 学习日期: 2024-XX-XX

# 创建字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

# 访问字典
print(f"姓名: {person['name']}")
print(f"年龄: {person.get('age', 0)}")

# 添加和修改
person["email"] = "zhangsan@example.com"
person["age"] = 26
print(f"更新后: {person}")

# 删除键值对
removed_city = person.pop("city")
print(f"被移除的城市: {removed_city}")
print(f"删除后: {person}")

# 字典方法
print(f"所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")
print(f"所有项: {list(person.items())}")

# 字典遍历
print("\n遍历字典:")
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式
squares = {x: x**2 for x in range(6)}
print(f"平方字典: {squares}")

# 嵌套字典
students = {
    "001": {
        "name": "小明",
        "scores": {"math": 90, "english": 85}
    },
    "002": {
        "name": "小红",
        "scores": {"math": 95, "english": 88}
    }
}

print(f"001号学生数学成绩: {students['001']['scores']['math']}")
