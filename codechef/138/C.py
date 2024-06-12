# -*- coding : utf-8 -*-
# @Time: 2024/6/12 22:41
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    if n == 1:
        print(1)
        continue

    nums = [3] * (n - 3) + [3, 2, 1]
    print(*nums)
    # x1 = nums[0]
    # x2 = nums[0]
    # for i in range(1, n):
    #     x1 = x1 & nums[i]
    #     x2 = x2 ^ nums[i]
    #     print(x1, x2, x1 >= x2)
    #
    # x1 = nums[-1]
    # x2 = nums[-1]
    # for i in range(n - 2, -1, -1):
    #     x1 = x1 & nums[i]
    #     x2 = x2 ^ nums[i]
    #     print(x1, x2, x1 <= x2)
