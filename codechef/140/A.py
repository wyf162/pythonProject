# -*- coding : utf-8 -*-
# @Time: 2024/6/26 22:29
# @Author: yefei.wang
# @File: A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    A = LI()
    B = LI()
    cnt = [0] * m
    for a in A:
        cnt[a % m] += 1
    ans = 0
    for b in B:
        ans += cnt[(m - b % m) % m]
    print(ans)
