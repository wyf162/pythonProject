# -*- coding : utf-8 -*-
# @Time: 2024/6/8 10:09
# @Author: yefei.wang
# @File: 1056B.py

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

tcn = 3
for _tcn_ in range(tcn):
    n, m = MI()
    c1 = n // m
    c2 = n % m
    ans = 0
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if (i * i + j * j) % m == 0:
                ans += c1 * c1
    for i in range(1, c2 + 1):
        for j in range(1, m + 1):
            if (i * i + j * j) % m == 0:
                ans += c1 * 2
    for i in range(1, c2 + 1):
        for j in range(1, c2 + 1):
            if (i * i + j * j) % m == 0:
                ans += 1
    print(ans)
