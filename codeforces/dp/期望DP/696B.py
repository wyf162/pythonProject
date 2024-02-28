# -*- coding: utf-8 -*-
# @Time: 2024/2/28 9:30
# @Author: yfwang
# @File: 696B.py
# https://codeforces.com/problemset/problem/696/B

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

n = I()

p = [0] * 2 + LI()
val = [1] * (n + 1)
for i in range(n, 1, -1):
    val[p[i]] += val[i]

ans = [0] * (n+1)
ans[1] = 1
for i in range(2, n+1):
    ans[i] = ans[p[i]] + (val[p[i]] - val[i] + 1) / 2

print(*ans[1:])
