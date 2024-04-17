# -*- coding: utf-8 -*-
# @Time: 2024/4/17 9:13
# @Author: yfwang
# @File: 1065C.py
# https://codeforces.com/problemset/problem/1065/C


import sys

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

n, k = MI()
nums = LI()

nums.sort(reverse=True)
mx = max(nums)
mi = min(nums)
if mi == mx:
    print(0)
    exit()

ans = 1
tot = 0
cnt = 0

i = 0
while i < n:
    cost = tot - cnt * nums[i]
    if cost <= k:
        tot += nums[i]
        cnt += 1
        i += 1
    else:
        hi = (tot - k + cnt - 1) // cnt
        ans += 1
        tot = hi * cnt
        if hi <= mi:
            break
print(ans)
