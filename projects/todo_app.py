# -*- coding: utf-8 -*-
# 待办事项应用
# 学习日期: 2024-XX-XX

import json
import os
from datetime import datetime

class TodoApp:
    """待办事项应用"""
    
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = []
        self.load_todos()
    
    def load_todos(self):
        """从文件加载待办事项"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
            except Exception as e:
                print(f"加载待办事项失败: {e}")
                self.todos = []
    
    def save_todos(self):
        """保存待办事项到文件"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存待办事项失败: {e}")
    
    def add_todo(self, task):
        """添加待办事项"""
        todo = {
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"已添加: {task}")
    
    def complete_todo(self, index):
        """完成待办事项"""
        if 0 <= index < len(self.todos):
            self.todos[index]['completed'] = True
            self.todos[index]['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_todos()
            print(f"已完成: {self.todos[index]['task']}")
        else:
            print("无效的索引")
    
    def delete_todo(self, index):
        """删除待办事项"""
        if 0 <= index < len(self.todos):
            deleted = self.todos.pop(index)
            self.save_todos()
            print(f"已删除: {deleted['task']}")
        else:
            print("无效的索引")
    
    def list_todos(self):
        """列出所有待办事项"""
        if not self.todos:
            print("没有待办事项")
            return
        
        print("\n=== 待办事项列表 ===")
        for i, todo in enumerate(self.todos):
            status = "[完成]" if todo['completed'] else "[待办]"
            print(f"{i}. {status} {todo['task']}")
            if todo['completed'] and 'completed_at' in todo:
                print(f"   完成于: {todo['completed_at']}")
            else:
                print(f"   创建于: {todo['created_at']}")

def interactive_todo():
    """交互式待办事项应用"""
    app = TodoApp()
    
    while True:
        print("\n=== 待办事项应用 ===")
        print("1. 查看所有待办事项")
        print("2. 添加新待办事项")
        print("3. 完成待办事项")
        print("4. 删除待办事项")
        print("5. 退出")
        
        choice = input("\n请选择操作 (1-5): ").strip()
        
        if choice == '1':
            app.list_todos()
        elif choice == '2':
            task = input("输入待办事项: ").strip()
            if task:
                app.add_todo(task)
            else:
                print("待办事项不能为空")
        elif choice == '3':
            app.list_todos()
            index = input("输入要完成的待办事项编号: ").strip()
            try:
                app.complete_todo(int(index))
            except ValueError:
                print("请输入有效的数字")
        elif choice == '4':
            app.list_todos()
            index = input("输入要删除的待办事项编号: ").strip()
            try:
                app.delete_todo(int(index))
            except ValueError:
                print("请输入有效的数字")
        elif choice == '5':
            print("再见！")
            break
        else:
            print("无效的选择，请重新输入")

# 取消下面这行的注释可以运行待办事项应用
# interactive_todo()
