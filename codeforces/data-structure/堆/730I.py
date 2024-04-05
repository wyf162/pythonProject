# -*- coding : utf-8 -*-
# @Time: 2024/4/5 11:54
# @Author: yefei.wang
# @File: 730I.py
# https://codeforces.com/problemset/problem/730/I

import sys
from heapq import nsmallest, heapify, heappop, heappush
from math import inf

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

n, p, s = MI()
nums1 = LI()
nums2 = LI()

used = [0] * n

v1 = nsmallest(p, (-nums1[i] * n + i for i in range(n)))
ans = 0
for x in v1:
    ans -= x // n
    used[x % n] = 1

v1 = [-nums1[i] * n + i for i in range(n) if not used[i]]
v2 = [-nums2[i] * n + i for i in range(n) if not used[i]]
to_12 = [-(nums2[i] - nums1[i]) * n + i for i in range(n) if used[i]]

heapify(v1)
heapify(v2)
heapify(to_12)

for _ in range(s):
    while v1 and used[v1[0] % n] != 0: heappop(v1)
    while v2 and used[v2[0] % n] != 0: heappop(v2)
    while to_12 and used[to_12[0] % n] != 1: heappop(to_12)

    method1 = -(v2[0] // n) if v2 else -inf
    method2 = -(v1[0] // n) - (to_12[0] // n) if v1 and to_12 else -inf

    if method1 >= method2:
        ans += method1
        used[heappop(v2) % n] = 2
    else:
        ans += method2
        i = heappop(v1) % n
        used[i] = 1
        heappush(to_12, -(nums2[i] - nums1[i]) * n + i)
        used[heappop(to_12) % n] = 2

print(ans)
print(' '.join(str(i + 1) for i in range(n) if used[i] == 1))
print(' '.join(str(i + 1) for i in range(n) if used[i] == 2))
