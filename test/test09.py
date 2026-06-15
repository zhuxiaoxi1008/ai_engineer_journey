# print(int('11', base=8))

# 偏函数
from functools import partial

int2 = partial[int](int, base=2)
# print(int2('1010'))

max10 = partial(max,  10)
# print(max10(5,7,9, 12))
import myPackage.web as web

web.init()

