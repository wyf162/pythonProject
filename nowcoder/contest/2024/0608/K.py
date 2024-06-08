# -*- coding : utf-8 -*-
# @Time: 2024/6/8 21:36
# @Author: yefei.wang
# @File: K.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
ops = [LI() for _ in range(m)]
mx = 10 ** 5
d = [0] * (n + 2 * mx + 5)
d2 = [0] * (n + 2 * mx + 5)

for i in range(m):
    a, b, c = ops[i]
    b += mx
    l = b - c + 1
    r = b + c - 1
    d2[l] += a
    d2[b + 1] -= 2 * a
    d2[r + 2] += a

for i in range(n + mx + 1):
    if i > 0:
        d2[i] += d2[i - 1]
        d[i] += d[i - 1] + d2[i]
    else:
        d[i] += d2[i]

print(*d[mx + 1:mx + 1 + n])
