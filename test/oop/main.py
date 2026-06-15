# main.py
from student import Student  # 直接从模块中导入 Student 类

def test():
    s1 = Student('Bart', 90)  # 现在可以直接使用 Student
    s2 = Student('Lisa', 85)
    s1.printScore()
    s2.printScore()

if __name__ == '__main__':
    test()