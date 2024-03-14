# -*- coding: utf-8 -*-
# @Time: 2024/3/14 13:53
# @Author: yfwang
# @File: 1941E.py

# https://codeforces.com/contest/1941/problem/E

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m, k, d = MI()
    mtx = [LI() for _ in range(n)]
    costs = []
    for idx in range(n):
        row = mtx[idx]

        dp = [0] * m
        dp[0] = 1
        mono_queue = deque()
        mono_queue.append((0, dp[0]))
        for i in range(1, m):
            while mono_queue[0][0] < i - d - 1:
                mono_queue.popleft()
            dp[i] = mono_queue[0][1] + row[i] + 1

            while mono_queue and mono_queue[-1][1] >= dp[i]:
                mono_queue.pop()
            mono_queue.append((i, dp[i]))

        costs.append(dp[-1])
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + costs[i]

    ret = pre_sum[k]
    for i in range(k, n+1):
        ret = min(ret, pre_sum[i] - pre_sum[i - k])
    print(ret)
