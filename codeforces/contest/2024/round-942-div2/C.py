# -*- coding : utf-8 -*-
# @Time: 2024/4/30 23:28
# @Author: yefei.wang
# @File: C.py

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
    n, k = MI()
    A = LI()
    A.sort()
    tot = sum(A)
    B = []
    for i in range(n - 1, -1, -1):
        avg = (k + tot) // (i + 1)
        if A[i] > avg:
            B.append(A[i])
        else:
            B.append(avg)
            k -= avg - A[i]
        tot -= A[i]
    B.sort()

    ans = B[0] * n - (n - 1) + n - B.count(B[0])
    print(ans)
