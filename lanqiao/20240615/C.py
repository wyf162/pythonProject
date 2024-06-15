# -*- coding : utf-8 -*-
# @Time: 2024/6/15 19:41
# @Author: yefei.wang
# @File: C.py


from heapq import nsmallest

import os
import sys

# 请在此输入您的代码
sys.stdin = open('../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
A = LI()
queries = [LI() + [i] for i in range(q)]
ans = [0] * n

for k, m, i in queries:
    B = []
    for a in A:
        if a <= k:
            B.append(a)
        else:
            B.append(2 * k - a)
    rets = nsmallest(m, B)
    print(sum(rets))



