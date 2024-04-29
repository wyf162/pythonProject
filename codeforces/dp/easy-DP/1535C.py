# -*- coding : utf-8 -*-
# @Time: 2024/4/29 21:15
# @Author: yefei.wang
# @File: 1535C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    s = input()
    n = len(s)
    f0 = [0] * n
    f1 = [0] * n
    if s[0] == '0':
        f0[0] = 1
    elif s[0] == '1':
        f1[0] = 1
    else:
        f0[0] = 1
        f1[0] = 1

    for i in range(1, n):
        if s[i] == '0':
            f0[i] = f1[i - 1] + 1
        elif s[i] == '1':
            f1[i] = f0[i - 1] + 1
        else:
            f0[i] = f1[i - 1] + 1
            f1[i] = f0[i - 1] + 1
    ret = 0
    for i in range(n):
        ret += max(f0[i], f1[i])
    print(ret)
