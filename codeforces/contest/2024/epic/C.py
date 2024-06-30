# -*- coding : utf-8 -*-
# @Time: 2024/6/30 22:48
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    H = LI()
    ans = 0
    eq = 0
    cur = 0
    for i in range(n - 1, -1, -1):
        if H[i] > cur:
            cur = H[i]
            eq = 0
        elif H[i] == cur:
            eq += 1
        else:
            ans += cur + eq
            eq = 0
            cur = H[i]
    ans += cur + eq
    print(ans)
