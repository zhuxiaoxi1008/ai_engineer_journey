#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
' a test module ' # 第一个字符串是文档字符串，用于描述模块的功能

__author__ = 'zxx1008' # 作者

'''
python 的标准模板写法前四行
第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
第2行注释表示.py文件本身使用标准UTF-8编码；
'''

import sys

def test():
    args = sys.argv
    if len(args)==1: # argv至少有一个元素，因为第一个参数永远是该.py文件的名称
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def say():
    print('Hi, I am ', __name__)
    
# Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
if __name__=='__main__': 
    test()