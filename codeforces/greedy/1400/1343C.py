# -*- coding: utf-8 -*-
# @Time: 2024/5/27 9:00
# @Author: yfwang
# @File: 1343C.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    ans = [nums[0]]
    for i in range(1, n):
        if ans[-1] * nums[i] > 0:
            ans[-1] = max(ans[-1], nums[i])
        else:
            ans.append(nums[i])
    ret = sum(ans)
    print(ret)
