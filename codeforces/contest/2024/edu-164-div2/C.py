# -*- coding : utf-8 -*-
# @Time: 2024/4/12 22:55
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
    x = input()
    y = input()
    n1 = len(x)
    n2 = len(y)
    n = max(n1, n2)
    x = '0' * (n - n1) + x
    y = '0' * (n - n2) + y
    s1 = ''
    s2 = ''
    diff = False
    for i in range(n):
        if diff:
            s1 += min(x[i], y[i])
            s2 += max(x[i], y[i])
        else:
            if x[i] == y[i]:
                s1 += x[i]
                s2 += y[i]
                continue
            else:
                s1 += max(x[i], y[i])
                s2 += min(x[i], y[i])
                diff = True
    s1 = s1.replace('0', '')
    s2 = s2.replace('0', '')
    print(s1)
    print(s2)
