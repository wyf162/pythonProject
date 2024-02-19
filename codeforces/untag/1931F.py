# -*- coding : utf-8 -*-
# @Time: 2024/2/19 21:02
# @Author: yefei.wang
# @File: 1931F.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('./../input.txt', 'r')
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
    n, k = MI()
    ans = True
    if k == 1:
        nums = LI()
        YN(ans)
        continue

    A = [0] * (n + 1)
    nums = LI()
    for i in range(1, n):
        A[nums[i]] = i * 2

    undefine = nums[0]
    left = 0
    right = n * 2

    for _ in range(k - 1):
        nums = LI()
        for i in range(2, n):
            i1, i2 = nums[i - 1], nums[i]
            if i1 == undefine:
                right = A[i2] - 1
            elif i2 == undefine:
                left = A[i1] + 1
            else:
                if A[i1] > A[i2]:
                    ans = False
                    break
    if left > right:
        ans = False
    YN(ans)
