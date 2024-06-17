# -*- coding: utf-8 -*-
# @Time: 2024/6/17 9:23
# @Author: yfwang
# @File: 1077C.py

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

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    nums = [(x, i) for i, x in enumerate(A)]
    nums.sort()
    PA = [0]
    for x, _ in nums:
        PA.append(PA[-1] + x)

    ans = []
    for i in range(n-1):
        x, i1 = nums[i]
        if nums[-1][0] == PA[-2] - x:
            ans.append(i1)
    if PA[-3] == nums[-2][0]:
        ans.append(nums[-1][1])
    print(len(ans))
    print(' '.join(str(x+1) for x in ans))