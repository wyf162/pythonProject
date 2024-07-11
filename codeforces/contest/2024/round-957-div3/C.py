# -*- coding : utf-8 -*-
# @Time: 2024/7/11 22:43
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
    n, m, k = MI()
    pre = []
    mid = []
    suf = []
    for i in range(1, n + 1):
        if i <= m:
            suf.append(i)
        elif i >= k:
            pre.append(i)
        else:
            mid.append(i)
    ans = pre[::-1] + mid + suf
    print(*ans)
