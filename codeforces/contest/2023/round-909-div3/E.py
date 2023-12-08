# -*- coding : utf-8 -*-
# @Time: 2023/11/17 23:13
# @Author: yefei.wang
# @File: E.py

import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    mi_idx = 0
    for i in range(n):
        if a[i] < a[mi_idx]:
            mi_idx = i
    for i in range(mi_idx+1, n):
        if a[i] < a[i-1]:
            print(-1)
            break
    else:
        print(mi_idx)
