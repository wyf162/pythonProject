# -*- coding : utf-8 -*-
# @Time: 2023/9/24 22:53
# @Author: yefei.wang
# @File: f.py
import sys

sys.stdin = open('../../input.txt', 'r')


def I(): return int(input())


def II(): return map(int, input().split())


def LI(): return list(map(int, input().split()))


q, k = II()
qs = []
for _ in range(q):
    qs.append(input().split())


dp = [0 for _ in range(k + 1)]
dp[0] = 1
mod = 998244353

for op, x in qs:
    x = int(x)
    if op == '+':
        for j in range(k, x-1, -1):
            dp[j] += dp[j - x]
            dp[j] %= mod
    else:
        for j in range(x, k+1, 1):
            dp[j] -= dp[j - x]
            dp[j] %= mod

    print(dp[-1])
