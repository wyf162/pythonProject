# -*- coding : utf-8 -*-
# @Time: 2024/3/27 22:53
# @Author: yefei.wang
# @File: C.py

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
    n = I()
    nums1 = list(input())
    nums2 = list(input())
    ca = []
    ac = []
    b = []
    ans = True

    for i in range(n):
        if nums1[i] == nums2[i]:
            if nums1[i] == 'b':
                b.append(i)
            continue
        elif nums1[i] == 'c' and nums2[i] == 'a':
            ca.append(i)
        elif nums1[i] == 'a' and nums2[i] == 'c':
            ac.append(i)
        else:
            ans = False
            break

    if len(ca) == 0 and len(ac) == 0:
        pass
    elif len(ca) == len(ac) and b:
        j = 0
        for i in range(len(ca)):
            while j < len(b):
                if ac[i] < b[j] < ca[i]:
                    break
                else:
                    j += 1
        if j >= len(b):
            ans = False
    else:
        ans = False
    YN(ans)
