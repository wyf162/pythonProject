# -*- coding : utf-8 -*-
# @Time: 2024/6/15 20:37
# @Author: yefei.wang
# @File: E.py


import math
import os
import sys
from itertools import accumulate

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, minlen = MI()
A = LI()
PA = list(accumulate(A, initial=0))

# 同一右端点的子数组 有logM个不同的gcd
# 要计算每个gcd 最远可以到哪里

tmp = []
idx = []
ans = 0

for i in range(n):
    k = len(tmp)
    g = A[i]

    for j in range(k - 1, -1, -1):
        g = math.gcd(g, tmp[j])
        tmp[j] = g

    tmp.append(A[i])
    idx.append(i)

    ntmp = []
    nidx = []

    for j in range(k + 1):
        if len(ntmp) == 0 or ntmp[-1] != tmp[j]:
            ntmp.append(tmp[j])
            nidx.append(idx[j])

    tmp = ntmp
    idx = nidx

    for j in range(len(tmp)):
        if i - idx[j] + 1 >= minlen:
            ans = max(ans, (PA[i + 1] - PA[idx[j]]) * tmp[j])
print(ans)
