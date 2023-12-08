# -*- coding : utf-8 -*-
# @Time: 2023/12/2 21:05
# @Author: yefei.wang
# @File: E.py


import sys
from heapq import heappop, heappush

# sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N, M, L = MI()
A = LI()
B = LI()

nums1 = [[-x, i] for i, x in enumerate(A)]
nums2 = [[-x, i] for i, x in enumerate(B)]

s = set()
for _ in range(L):
    u, v = GMI()
    s.add((u, v))

nums1.sort()
nums2.sort()

h = [(nums1[0][0] + nums2[0][0], 0, 0)]
while h:
    _, i, j = heappop(h)
    if (nums1[i][1], nums2[j][1]) not in s:
        print(-nums1[i][0] - nums2[j][0])
        break
    if j == 0 and i + 1 < len(nums1):
        heappush(h, (nums1[i + 1][0] + nums2[0][0], i + 1, 0))
    if j + 1 < len(nums2):
        heappush(h, (nums1[i][0] + nums2[j + 1][0], i, j + 1))
