# -*- coding : utf-8 -*-
# @Time: 2023/12/2 19:56
# @Author: yefei.wang
# @File: A.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

M, D = MI()
y, m, d = MI()
if m == M and d == D:
    print(y + 1, 1, 1)
elif d == D:
    print(y, m+1, 1)
else:
    print(y, m, d+1)

