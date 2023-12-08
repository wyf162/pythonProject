# -*- coding : utf-8 -*-
# @Time: 2023/11/11 19:02
# @Author: yefei.wang
# @File: C.py


import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

hst = '3456789XJQKA2MF'

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    s1, s2 = s.split(' ')
    x1, x2 = s1[0], s1[1]
    y1, y2 = s2[0], s2[1]
    i1 = hst.index(x1)
    i2 = hst.index(x2)
    j1 = hst.index(y1)
    j2 = hst.index(y2)
    if x1 == x2:
        print('ShallowDream')
    elif (i2 >= j1 and i2 >= j2) or (i1 >= j1 and i1 >= j2):
        print('ShallowDream')
    else:
        print('Joker')
