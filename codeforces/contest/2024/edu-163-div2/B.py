# -*- coding : utf-8 -*-
# @Time: 2024/3/15 22:42
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
    n = I()
    nums = LI()
    x = nums[-1]
    ans = True
    for i in range(n-2, -1, -1):
        if nums[i] <= x:
            x = nums[i]
        else:
            ss = [int(c) for c in str(nums[i])]
            for y in ss[::-1]:
                if y <= x:
                    x = y
                else:
                    ans = False
        if ans is False:
            break
    YN(ans)
