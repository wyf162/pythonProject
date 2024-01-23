# -*- coding : utf-8 -*-
# @Time: 2023/10/14 11:59
# @Author: yefei.wang
# @File: 1619E.py

import sys
from heapq import heappop, heappush

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    a.sort()
    dp = [-1] * (n + 1)
    pq = []
    j = 0
    op = 0
    for i in range(n + 1):
        if i > 0:
            if pq:
                x = -heappop(pq)
                op += i - 1 - x
            else:
                break
        t = 0
        while j < n and a[j] == i:
            heappush(pq, -i)
            t += 1
            j += 1
        dp[i] = t + op

    print(' '.join(map(str, dp)))
