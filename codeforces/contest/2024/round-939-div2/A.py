# -*- coding : utf-8 -*-
# @Time: 2024/4/13 22:34
# @Author: yefei.wang
# @File: A.py

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
    n1, n2 = MI()
    nums1 = LI()
    nums2 = LI()
    ans = []
    for i in range(n2):
        if nums2[i] < nums1[0]:
            ans.append(nums2[i])
        else:
            ans.append(nums1[0] - 1)
    print(*ans)
