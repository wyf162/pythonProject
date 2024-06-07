# -*- coding : utf-8 -*-
# @Time: 2024/6/6 22:48
# @Author: yefei.wang
# @File: C.py
# lcm

import sys
import math

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
    nums = LI()
    z = math.lcm(*nums)
    tot = 0
    for i in range(n):
        tot += z // nums[i]

    if tot >= z:
        print(-1)
    else:
        ans = [z // nums[i] for i in range(n)]
        print(' '.join(str(x) for x in ans))
