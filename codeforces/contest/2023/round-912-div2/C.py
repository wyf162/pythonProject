# -*- coding : utf-8 -*-
# @Time: 2023/12/1 1:29
# @Author: yefei.wang
# @File: C.py

import sys

sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    pre_sum = [0] * (n+1)
    for i in range(n):
        pre_sum[i+1] = pre_sum[i] + a[i]

