# -*- coding : utf-8 -*-
# @Time: 2024/5/24 21:12
# @Author: yefei.wang
# @File: 1512G.py
# 积性函数 质因子

import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 10

div = [1] * (10 ** 7 + 1)
for i in range(2, 10 ** 7 + 1):
    if div[i] == 1:
        div[i] = i
        for j in range(i * i, 10 ** 7 + 1, i):
            div[j] = i

phi = [1] * (10 ** 7 + 1)
for i in range(2, 10 ** 7 + 1):
    x = 0
    v = 1
    while i % v == 0:
        x += v
        v *= div[i]
    v //= div[i]
    phi[i] = phi[i // v] * x

ans = [-1] * (10 ** 7 + 1)
for i in range(1, 10 ** 7 + 1):
    if phi[i] <= 10 ** 7 and ans[phi[i]] == -1:
        ans[phi[i]] = i


tcn = I()
for _tcn_ in range(tcn):
    x = I()
    print(ans[x])
