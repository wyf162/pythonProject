# -*- coding : utf-8 -*-
# @Time: 2024/5/18 10:04
# @Author: yefei.wang
# @File: 1056D.py
import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    tree = [[] for _ in range(n)]
    fa = LGMI()
    for i, x in enumerate(fa, start=1):
        tree[x].append(i)
    isleaf = [int(len(tree[i]) == 0) for i in range(n)]
    dfs = []
    stk = [0]
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in tree[x]:
            stk.append(y)
    dp = [0] * n
    for x in dfs[::-1]:
        dp[x] += isleaf[x]
        if x > 0:
            y = fa[x-1]
            dp[y] += dp[x]
    dp.sort()
    print(*dp)

