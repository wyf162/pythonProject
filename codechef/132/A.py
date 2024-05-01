# -*- coding : utf-8 -*-
# @Time: 2024/5/1 22:30
# @Author: yefei.wang
# @File: A.py

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
    n, m = MI()
    nums1 = LI() + [0] * 11
    nums2 = LI() + [0] * 11
    if n + m < 11 or n < 4 or m < 4:
        print(-1)
        continue
    nums1.sort()
    nums2.sort()
    tot = 0
    for i in range(4):
        tot += nums1.pop()
        tot += nums2.pop()
    for i in range(3):
        if nums1[-1] > nums2[-1]:
            tot += nums1.pop()
        else:
            tot += nums2.pop()
    print(tot)
