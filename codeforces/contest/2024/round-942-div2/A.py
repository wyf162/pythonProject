# -*- coding : utf-8 -*-
# @Time: 2024/4/30 22:35
# @Author: yefei.wang
# @File: A.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    B = LI()
    i = 0
    ans = 0
    for j in range(n):
        if A[i] <= B[j]:
            i += 1
            continue
        else:
            ans += 1
    print(ans)
