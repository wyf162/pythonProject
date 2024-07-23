# -*- coding : utf-8 -*-
# @Time: 2024/7/23 22:46
# @Author: yefei.wang
# @File: B1.py

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
    n, m = MI()
    A = LI()
    A.sort()
    i1 = 0
    tot = 0
    ans = 0
    for i2 in range(n):
        tot += A[i2]
        while i1 <= i2 and (A[i2] - A[i1] > 1 or tot > m):
            tot -= A[i1]
            i1 += 1
        ans = max(ans, tot)
    print(ans)
