# -*- coding : utf-8 -*-
# @Time: 2024/2/29 22:41
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
    nums1 = list(int(x) for x in input())
    nums2 = list(int(x) for x in input())
    f1 = [0] * n
    f2 = [0] * n
    f1[0] = 1
    if nums2[0] <= nums2[1]:
        f2[0] = 1
    # if nums1[1] <= nums2[0]:
    #     f1[1] = 1

    nums = [nums1[0]]
    for i in range(1, n):
        if nums1[i] == nums2[i - 1]:
            f1[i] = f1[i - 1]
            f2[i] = f2[i - 1] + f1[i]
            nums.append(nums1[i])
        elif nums1[i] < nums2[i - 1]:
            f1[i] = f1[i - 1]
            f2[i] = f1[i]
            nums.append(nums1[i])
        elif nums2[i - 1] < nums1[i]:
            f2[i] = f2[i - 1]
            nums.append(nums2[i - 1])

    nums.append(nums2[-1])
    print(''.join(str(x) for x in nums))
    ret = f2[-1]
    print(ret)
