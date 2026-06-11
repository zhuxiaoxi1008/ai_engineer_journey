from functools import reduce

for x in [1,2,3,4,5]:
    # print(x)
    pass

l = iter([1,2,3,4,5])

# while True:
#     try:
#         print(next(l))
#     except StopIteration:
#         break
#         print("end")

# print(abs(-10))

def add(a,b,f):
    return f(a) + f(b)

# print(add(-5, 6, abs))

# test map reduce

l = [1,2,3,4,5]

def f(x):
    return x**2

# print(list(map(f,l)))

# print(list(map(str, [1,2,3,4,5])))

# print(list(map(lambda x: x**2, l)))


# print(reduce(lambda x,y: x+y, l))

# test1
def normalize(name):
    s = name.lower()
    s = s.title()
    return s

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
# print(L2)

# test2
from functools import reduce

def prod(L):
    return reduce(lambda x,y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# test 3
# 
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    '''
    将字符串转换为数字
    '''
    l = s.split('.')
    l[0] = list(map(lambda x: DIGITS[x], l[0]))
    l[1] = list(map(lambda x: DIGITS[x], l[1]))
    print(l)
    n1 = reduce(lambda x,y: x*10 +y, l[0])
    n2 = reduce(lambda x,y: x*10 + y, l[1]) * (0.1 ** len(l[1]))
  
    return n1+n2

# print(str2float('123.456'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!') 