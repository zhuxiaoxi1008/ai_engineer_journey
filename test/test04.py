def fact(n):
    if n == 1:
        return 1
    multi = n * fact(n - 1)
    return multi

# print(fact(1000))

# 汉诺塔的移动可以用递归函数非常简单地实现
def hanoi(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)

# hanoi(3, "A", "B", "C")

def initList(n):
    L = []
    for i in range(n):
        L.append(i + 1)
    return L

# print(initList(100))
# print([*range(100)])

def halfList(n):
    res = []
    while n > 0:
        res.append(n)
        n = n - 2
    return res

# print(len(halfList(100)))

l = list(range(100))
# print(len(l))

# # 取前 10 个元素
# print(l[:10:2])


def trim(s):
    if not s:  # 处理空字符串
        return ''
    
    # 去除开头空格
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    # 去除结尾空格
    end = len(s) - 1
    while end >= start and s[end] == ' ':
        end -= 1
    
    return s[start:end+1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
