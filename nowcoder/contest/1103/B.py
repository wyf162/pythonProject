# -*- coding : utf-8 -*-
# @Time: 2023/11/4 10:59
# @Author: yefei.wang
# @File: B.py
import sys

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    L, R, K = MI()
    if K == 0:
        rst = (R - L + 1) % 2
    else:
        x1 = L // 2
        x2 = (R + 1) // 2
        rst = (x2 - x1) % 2
    print(rst)
