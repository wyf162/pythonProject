# -*- coding: utf-8 -*-
# @Time: 2024/4/9 11:00
# @Author: yfwang
# @File: 631B.py
# https://codeforces.com/problemset/problem/613/B

import sys
from itertools import accumulate

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

n, a, cf, cm, m = MI()
nums = LI()
st_range = sorted(range(n), key=lambda x: nums[x])
acc = list(accumulate((nums[i] for i in st_range), initial=0))

equal = full = -1

for i in range(n + 1):
    tot = i * a - (acc[n] - acc[n - i])
    if tot > m: break
    if i == n:
        new_equal = a
        new_full = n
    else:
        resid = m - tot

        l, r = 1, n - i
        while l <= r:
            mid = (l + r) // 2
            if nums[st_range[mid - 1]] * mid - acc[mid] <= resid:
                l = mid + 1
            else:
                r = mid - 1

        new_equal = min(a, nums[st_range[r - 1]] + (resid - (nums[st_range[r - 1]] * r - acc[r])) // r)
        new_full = i

    if new_equal * cm + new_full * cf >= equal * cm + full * cf:
        equal = new_equal
        full = new_full

print(equal * cm + full * cf)
for i in range(n):
    if nums[i] < equal:
        nums[i] = equal

for i in range(full):
    nums[st_range[n - 1 - i]] = a

print(' '.join(map(str, nums)))
