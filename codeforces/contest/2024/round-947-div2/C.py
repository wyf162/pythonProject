# -*- coding : utf-8 -*-
# @Time: 2024/5/25 23:26
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
    A = LI()
    if n <= 3:
        A.sort()
        print(A[(n - 1) // 2])
        continue
    ans = 0
    for i in range(n - 2):
        t = A[i:i + 3]
        t.sort()
        ans = max(ans, t[1])
    print(ans)
