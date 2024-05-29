# -*- coding: utf-8 -*-
# @Time: 2024/5/29 11:14
# @Author: yfwang
# @File: 609D.py
# sortings two pointers

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
    n, m, k, s = MI()
    cost1, cost2 = LI(), LI()

    nums1, nums2 = [], []
    for i in range(1, m + 1):
        typ, x = MI()
        if typ == 1:
            nums1.append((x, i))
        else:
            nums2.append((x, i))
    n1, n2 = len(nums1), len(nums2)

    for i in range(1, n):
        cost1[i] = min(cost1[i], cost1[i - 1])
        cost2[i] = min(cost2[i], cost2[i - 1])

    nums1.sort()
    nums2.sort()
    L = 1
    R = n
    ans = n + 1
    while L <= R:
        mid = (L + R) // 2
        i1, i2 = 0, 0
        c1, c2 = cost1[mid - 1], cost2[mid - 1]
        tot = 0
        for _ in range(k):
            if i1 < n1 and i2 < n2:
                if nums1[i1][0] * c1 < nums2[i2][0] * c2:
                    tot += nums1[i1][0] * c1
                    i1 += 1
                else:
                    tot += nums2[i2][0] * c2
                    i2 += 1
            elif i1 < n1:
                tot += nums1[i1][0] * c1
                i1 += 1
            elif i2 < n2:
                tot += nums2[i2][0] * c2
                i2 += 1
        if tot <= s:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    if ans > n:
        print(-1)
        continue

    i1, i2 = 0, 0
    rets1, rets2 = [], []
    c1, c2 = cost1[ans - 1], cost2[ans - 1]
    tot = 0
    for _ in range(k):
        if i1 < n1 and i2 < n2:
            if nums1[i1][0] * c1 < nums2[i2][0] * c2:
                rets1.append(nums1[i1][1])
                i1 += 1
            else:
                rets2.append(nums2[i2][1])
                i2 += 1
        elif i1 < n1:
            rets1.append(nums1[i1][1])
            i1 += 1
        elif i2 < n2:
            rets2.append(nums2[i2][1])
            i2 += 1

    print(ans)
    d1 = cost1.index(c1) + 1
    d2 = cost2.index(c2) + 1
    for x in rets1:
        print(x, d1)
    for x in rets2:
        print(x, d2)
