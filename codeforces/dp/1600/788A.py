# -*- coding : utf-8 -*-
# @Time: 2024/6/8 12:20
# @Author: yefei.wang
# @File: 788A.py

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

tcn = 1
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    diff = []
    for i in range(1, n):
        diff.append(abs(A[i] - A[i - 1]))
    nums1 = [x * (-1) ** i for i, x in enumerate(diff)]
    nums2 = [x * (-1) ** (i + 1) for i, x in enumerate(diff)]


    def f(nums):
        mx = 0
        cur = 0
        for x in nums:
            cur += x
            mx = max(mx, cur)
            cur = max(cur, 0)
        return mx


    ans1 = f(nums1)
    ans2 = f(nums2)
    ans = max(ans1, ans2)
    print(ans)
