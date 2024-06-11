# -*- coding : utf-8 -*-
# @Time: 2024/6/12 0:51
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
    ans = n
    mx = n
    for x in range(2, n):
        tot = 0
        k = 1
        while x * k <= n:
            tot += x * k
            k += 1
        if tot > mx:
            mx = tot
            ans = x
    print(ans)
