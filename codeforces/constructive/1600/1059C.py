# -*- coding : utf-8 -*-
# @Time: 2024/7/13 12:08
# @Author: yefei.wang
# @File: 1059C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 10
for _tcn_ in range(tcn):
    N = I()
    nums = []
    x = 1
    n = N
    while n:
        nums += [x] * ((n + 1) // 2)
        n -= ((n + 1) // 2)
        x *= 2
    if len(nums) >= 2:
        nums[-1] = N // nums[-2] * nums[-2]
    print(*nums)
