# -*- coding : utf-8 -*-
# @Time: 2024/6/30 22:38
# @Author: yefei.wang
# @File: B.py

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
    A = LI()
    mx = A[0]
    B = []
    for i in range(1, n):
        if A[i]>=mx:
            mx = A[i]
        else:
            B.append(mx - A[i])
    # print(B)
    B.sort()
    ans = 0
    cur = 0
    m = len(B)
    for i in range(m):
        ans += (B[i] - cur) * (m - i + 1)
        cur = B[i]
    print(ans)



