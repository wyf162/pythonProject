# -*- coding: utf-8 -*-
# @Time: 2024/3/14 14:27
# @Author: yfwang
# @File: 1941F.py
# https://codeforces.com/contest/1941/problem/F

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    n, m, k = MI()
    nums1 = LI()
    nums2 = LI()
    nums3 = LI()
    nums1.sort()
    nums2.sort()
    nums3.sort()

    diff = []
    for i in range(n - 1):
        diff.append(nums1[i + 1] - nums1[i])

    mx = max(diff)
    if diff.count(mx) > 1:
        print(mx)
        continue
    i1 = diff.index(mx)
    mid = (nums1[i1] + nums1[i1 + 1]) // 2

    i2 = m - 1
    i3 = 0
    v = nums2[i2] + nums3[i3]
    ret = mx

    while i2 >= 0 and i3 < k:
        v = nums2[i2] + nums3[i3]
        if nums1[i1] < v < nums1[i1 + 1]:
            ret = min(ret, max(v - nums1[i1], nums1[i1 + 1] - v))
        if v < mid:
            i3 += 1
        elif v > mid:
            i2 -= 1
        else:
            break
    diff.sort()

    if len(diff) > 1:
        ret = max(diff[-2], ret)
    print(ret)
