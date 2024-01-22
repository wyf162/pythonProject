# -*- coding : utf-8 -*-
# @Time: 2024/1/19 19:16
# @Author: yefei.wang
# @File: B.py

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
    s = input()
    t = input()
    if len(t) == 1:
        if s == t:
            print(10)
        else:
            print(0)
    else:
        for c in s:
            if c not in t:
                print(0)
                break
        else:
            print(10)