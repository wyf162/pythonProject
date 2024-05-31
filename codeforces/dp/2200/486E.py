# -*- coding: utf-8 -*-
# @Time: 2024/5/31 9:35
# @Author: yfwang
# @File: 486E.py
# LIS LDS

import sys
import bisect

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

n = I()
nums = LI()

pre = [0] * n
dp = []
for x, num in enumerate(nums):
    i = bisect.bisect_left(dp, num)
    pre[x] = i
    if 0 <= i < len(dp):
        dp[i] = num
    else:
        dp.append(num)
ceil = len(dp)
post = [0] * n
dp = []
for x in range(n - 1, -1, -1):
    num = -nums[x]
    i = bisect.bisect_left(dp, num)
    post[x] = i
    if 0 <= i < len(dp):
        dp[i] = num
    else:
        dp.append(num)

cnt = [0] * (ceil + 1)
ans = [0] * n
for i in range(n):
    if pre[i] + post[i] + 1 == ceil:
        cnt[pre[i]] += 1
    else:
        ans[i] = 1

for i in range(n):
    if ans[i]:
        continue
    if cnt[pre[i]] == 1:
        ans[i] = 3
    else:
        ans[i] = 2

print(''.join(str(x) for x in ans))

























