# -*- coding : utf-8 -*-
# @Time: 2024/3/31 15:29
# @Author: yefei.wang
# @File: 1942D.py
# https://codeforces.com/contest/1942/problem/A

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n, k = MI()
    if n == k:
        print(*[1 for _ in range(n)])
    elif k == 1:
        print(*[1+i for i in range(n)])
    else:
        print(-1)
