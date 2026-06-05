# -*- coding: utf-8 -*-
"""
清理乱码文件脚本
删除所有不带utf8_前缀的旧文件，保留utf8_前缀的正确文件
"""
import os
import shutil

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 需要删除的旧文件列表（不带utf8_前缀的文件）
OLD_FILES = [
    "basics/variables.py",
    "basics/control_flow.py",
    "basics/functions.py",
    "data_structures/lists.py",
    "data_structures/dictionaries.py",
    "oop/classes.py",
    "oop/inheritance.py",
    "advanced/decorators.py",
    "advanced/generators.py",
    "projects/calculator.py",
    "projects/todo_app.py",
    "notes/day1.md",
    "notes/day2.md",
    "notes/day3.md",
    "requirements.txt",
]

# 需要重命名的文件列表（utf8_前缀 -> 正常文件名）
RENAME_FILES = [
    ("basics/utf8_variables.py", "basics/variables.py"),
    ("basics/utf8_control_flow.py", "basics/control_flow.py"),
    ("basics/utf8_functions.py", "basics/functions.py"),
    ("data_structures/utf8_lists.py", "data_structures/lists.py"),
    ("data_structures/utf8_dictionaries.py", "data_structures/dictionaries.py"),
    ("oop/utf8_classes.py", "oop/classes.py"),
    ("oop/utf8_inheritance.py", "oop/inheritance.py"),
    ("advanced/utf8_decorators.py", "advanced/decorators.py"),
    ("advanced/utf8_generators.py", "advanced/generators.py"),
    ("projects/utf8_calculator.py", "projects/calculator.py"),
    ("projects/utf8_todo_app.py", "projects/todo_app.py"),
    ("notes/utf8_day1.md", "notes/day1.md"),
    ("notes/utf8_day2.md", "notes/day2.md"),
    ("notes/utf8_day3.md", "notes/day3.md"),
    ("utf8_requirements.txt", "requirements.txt"),
]

def cleanup():
    """执行清理操作"""
    print("=" * 50)
    print("清理乱码文件脚本")
    print("=" * 50)
    
    # 步骤1: 删除旧文件
    print("\n步骤1: 删除旧文件")
    for file_path in OLD_FILES:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path):
            try:
                os.remove(full_path)
                print(f"  已删除: {file_path}")
            except Exception as e:
                print(f"  删除失败: {file_path} - {e}")
        else:
            print(f"  文件不存在: {file_path}")
    
    # 步骤2: 重命名utf8_文件
    print("\n步骤2: 重命名utf8_文件")
    for old_name, new_name in RENAME_FILES:
        old_path = os.path.join(BASE_DIR, old_name)
        new_path = os.path.join(BASE_DIR, new_name)
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"  已重命名: {old_name} -> {new_name}")
            except Exception as e:
                print(f"  重命名失败: {old_name} -> {new_name} - {e}")
        else:
            print(f"  文件不存在: {old_name}")
    
    print("\n" + "=" * 50)
    print("清理完成！")
    print("=" * 50)

if __name__ == "__main__":
    cleanup()
