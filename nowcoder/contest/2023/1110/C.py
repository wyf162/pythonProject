# -*- coding : utf-8 -*-
# @Time: 2023/11/10 19:32
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m, x = MI()
a = LI()
b = LI()

d = a + b + [x]
d.sort()
print(d[len(d)//2])
