# -*- coding: utf-8 -*-
# @Time: 2024/2/21 10:46
# @Author: yfwang
# @File: 1917C.py
# https://codeforces.com/problemset/problem/1917/C

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n, k, d = MI()
    nums1 = LI()
    nums2 = LI()

    cnt = sum(int(nums1[i1] == i1 + 1) for i1 in range(n))
    ans = (d - 1) // 2 + cnt

    for i in range(n * 2):
        if d - i - 2 < 0:
            break
        j = nums2[i % k]
        for i1 in range(j):
            nums1[i1] += 1

        cnt = sum(int(nums1[i1] == i1 + 1) for i1 in range(n))
        ans = max(ans, cnt + (d - i - 2) // 2)
    print(ans)
