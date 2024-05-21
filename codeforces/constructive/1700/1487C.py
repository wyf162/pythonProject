# -*- coding : utf-8 -*-
# @Time: 2024/4/19 19:25
# @Author: yefei.wang
# @File: 1487C.py
# https://codeforces.com/contest/1487/problem/C
# sortings

import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('../input.txt', 'r')
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
    rets = []
    if n % 2 == 1:
        for i in range(n):
            for j in range(i+1, n):
                if j - i <= n // 2:
                    rets.append(1)
                else:
                    rets.append(-1)
    else:
        for i in range(n):
            for j in range(i+1, n):
                if j - i < n // 2:
                    rets.append(1)
                elif j - i == n // 2:
                    rets.append(0)
                else:
                    rets.append(-1)
    print(' '.join(str(x) for x in rets))
