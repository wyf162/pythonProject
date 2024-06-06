# -*- coding : utf-8 -*-
# @Time: 2024/6/6 22:40
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
    x, y = MI()
    s1 = list(bin(x)[2:])
    s2 = list(bin(y)[2:])
    s1.reverse()
    s2.reverse()
    # print(s1)
    # print(s2)
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] == s2[i]:
            i += 1
        else:
            break
    if i == len(s1):
        while s2[i] == '0':
            i += 1
    elif i == len(s2):
        while s1[i] == '0':
            i += 1
    print(1 << i)
