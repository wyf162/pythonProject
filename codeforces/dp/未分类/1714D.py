# -*- coding : utf-8 -*-
# @Time: 2024/1/4 22:52
# @Author: yefei.wang
# @File: 1714D.py

import sys

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
    t = input()
    m = len(t)
    n = I()
    ss = [input() for _ in range(n)]
    mtx = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if t[i:].startswith(ss[j]):
                mtx[i].append(j)
    dp = [0] + [m + 1] * m
    for i in range(m):
        for j in mtx[i]:
            j1 = i + len(ss[j])
            if j1 <= m:
                dp[j1] = min(dp[i] + 1, dp[j1])
                for k in range(i + 1, j1):
                    dp[k] = min(dp[k], dp[j1])
    # print(dp)

    if dp[-1] < m + 1:
        print(dp[-1])
        i = 0
        for _ in range(dp[-1]):
            for j in range(n):
                find = False
                for j1 in range(i+1, i + len(ss[j])):
                    if j1 <= m and t[j1 - len(ss[j]):j1] == ss[j] and dp[j1] == dp[i] + 1:
                        print(j + 1, i+1)
                        i += len(ss[j])
                        find = True
                        break
                if find:
                    break
    else:
        print(-1)
