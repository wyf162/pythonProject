# -*- coding : utf-8 -*-
# @Time: 2024/6/26 22:36
# @Author: yefei.wang
# @File: B.py

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
    nums = []

    if n % 2:
        nums.append(n)
        n -= 1
    i = 1
    j = n
    while i <= j:
        nums.append(i)
        nums.append(j)
        i += 1
        j -= 1
    if len(nums) >= 2 and nums[-1] == nums[-2]:
        nums.pop()
    print(*nums)
