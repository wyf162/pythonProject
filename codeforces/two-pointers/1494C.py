# -*- coding : utf-8 -*-
# @Time: 2024/4/20 15:09
# @Author: yefei.wang
# @File: 1494C.py
import bisect
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
    A = LI()
    B = LI()


    def solve(nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        f = [0] * (n2 + 1)
        i1 = n1 - 1
        for i2 in range(n2 - 1, -1, -1):
            while i1 >= 0 and nums1[i1] > nums2[i2]:
                i1 -= 1
            if i1 >= 0 and nums1[i1] == nums2[i2]:
                f[i2] = f[i2 + 1] + 1
            else:
                f[i2] = f[i2 + 1]
        ans = f[0]
        i1 = 0
        for i2 in range(n2):
            while i1 < n1 and nums1[i1] <= nums2[i2]:
                i1 += 1
            idx = bisect.bisect_right(nums2, nums2[i2] - i1)
            ans = max(ans, i2 - idx + 1 + f[i2 + 1])
        return ans


    A1, A2 = [], []
    B1, B2 = [], []
    for a in A:
        if a < 0:
            A1.append(abs(a))
        else:
            A2.append(a)

    for b in B:
        if b < 0:
            B1.append(abs(b))
        else:
            B2.append(b)
    A1.reverse()
    B1.reverse()

    ret1 = solve(A1, B1)
    ret2 = solve(A2, B2)
    ret = ret1 + ret2
    # print(ret1, ret2)
    print(ret)
