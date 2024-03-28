# -*- coding : utf-8 -*-
# @Time: 2024/3/27 22:40
# @Author: yefei.wang
# @File: B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n, x = MI()
    nums = []
    y = x + x
    while n and y <= 10 ** 9:
        nums.append(y)
        n -= 1
        y += x
    y = 1
    while n:
        nums.append(y)
        n -= 1
        y += 1
    print(*nums)
