# -*- coding : utf-8 -*-
# @Time: 2024/5/23 21:49
# @Author: yefei.wang
# @File: 510D.py
# https://codeforces.com/contest/510/problem/D

import math
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
inf = 10 ** 10

tcn = 4
for _tcn_ in range(tcn):
    n = I()
    L = LI()
    C = LI()
    ans = inf
    cnt = dict()
    for i in range(n):
        for j in range(i + 1, n):
            g = math.gcd(L[i], L[j])
            if g == 1:
                ans = min(ans, C[i] + C[j])
            else:
                if g in cnt:
                    cnt[g] = C[i] + C[j]
                else:
                    cnt[g] = min(cnt[g], C[i] + C[j])

    if ans < inf:
        print(ans)
    else:
        print(-1)
