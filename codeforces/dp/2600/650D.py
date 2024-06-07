# -*- coding: utf-8 -*-
# @Time: 2024/6/7 9:33
# @Author: yfwang
# @File: 650D.py
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

n, m = MI()
nums = LI()
queries = [LI() for _ in range(m)]
g = [[] for _ in range(n)]
for i in range(m):
    p, x = queries[i][0] - 1, queries[i][1]
    g[p].append((x, i))

left = [0] * m
pre = [0] * n
dp = []
for i, num in enumerate(nums):
    for x, i1 in g[i]:
        i2 = bisect.bisect_left(dp, x)
        left[i1] = i2

    j = bisect.bisect_left(dp, num)
    pre[i] = j
    if 0 <= j < len(dp):
        dp[j] = num
    else:
        dp.append(num)
ceil = len(dp)
right = [0] * m
post = [0] * n
dp = []
for i in range(n - 1, -1, -1):
    num = -nums[i]
    for x, i1 in g[i]:
        i2 = bisect.bisect_left(dp, -x)
        right[i1] = i2

    j = bisect.bisect_left(dp, num)
    post[i] = j
    if 0 <= j < len(dp):
        dp[j] = num
    else:
        dp.append(num)

cnt = [0] * (ceil + 1)
useless = [0] * n
for i in range(n):
    if pre[i] + post[i] + 1 == ceil:
        cnt[pre[i]] += 1
    else:
        useless[i] = 1

for i in range(n):
    if useless[i]:
        continue
    if cnt[pre[i]] == 1:
        useless[i] = 3
    else:
        useless[i] = 2
# print(left)
# print(right)

ans = [ceil - 1] * m
for i in range(m):
    p, x = queries[i][0] - 1, queries[i][1]
    if useless[p] <= 2:
        ans[i] = max(ans[i], ceil)
    ans[i] = max(ans[i], left[i] + right[i] + 1)

print('\n'.join(str(x) for x in ans))
