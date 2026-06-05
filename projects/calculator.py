# -*- coding: utf-8 -*-
# 简易计算器
# 学习日期: 2024-XX-XX

class Calculator:
    """计算器类"""
    
    def add(self, a, b):
        """加法"""
        return a + b
    
    def subtract(self, a, b):
        """减法"""
        return a - b
    
    def multiply(self, a, b):
        """乘法"""
        return a * b
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    
    def power(self, base, exponent):
        """幂运算"""
        return base ** exponent
    
    def sqrt(self, number):
        """平方根"""
        if number < 0:
            raise ValueError("不能计算负数的平方根")
        return number ** 0.5

# 使用计算器
calc = Calculator()

print("计算器示例:")
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"2 ** 8 = {calc.power(2, 8)}")
print(f"√16 = {calc.sqrt(16)}")

# 交互式计算器
def interactive_calculator():
    """交互式计算器"""
    print("\n=== 交互式计算器 ===")
    print("支持的操作: +, -, *, /, ^ (幂), √ (平方根)")
    print("输入 'q' 退出")
    
    while True:
        try:
            expression = input("\n请输入表达式 (例如: 5 + 3): ").strip()
            
            if expression.lower() == 'q':
                print("再见！")
                break
            
            # 处理平方根
            if '√' in expression:
                num = float(expression.replace('√', '').strip())
                result = calc.sqrt(num)
                print(f"结果: {result}")
                continue
            
            # 处理其他运算
            parts = expression.split()
            if len(parts) != 3:
                print("错误: 请输入两个数字和一个运算符")
                continue
            
            a, op, b = parts
            a, b = float(a), float(b)
            
            if op == '+':
                result = calc.add(a, b)
            elif op == '-':
                result = calc.subtract(a, b)
            elif op == '*':
                result = calc.multiply(a, b)
            elif op == '/':
                result = calc.divide(a, b)
            elif op == '^':
                result = calc.power(a, b)
            else:
                print(f"错误: 不支持的操作符 '{op}'")
                continue
            
            print(f"结果: {result}")
            
        except ValueError as e:
            print(f"错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")

# 取消下面这行的注释可以运行交互式计算器
# interactive_calculator()
