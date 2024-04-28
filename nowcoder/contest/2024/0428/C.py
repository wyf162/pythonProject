# -*- coding : utf-8 -*-
# @Time: 2024/4/28 19:15
# @Author: yefei.wang
# @File: C.py

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

n = I()
nums = LI()
x = I()
cnt = [0] * 20

dp = [1, 3, 9]
while dp[-1] < 10 ** 9:
    dp.append(dp[-1] * 3)
# print(dp)
# print(len(dp))

for num in nums:
    for c in range(20):
        if dp[c] * x - dp[c] + 1 <= num <= dp[c] * x:
            cnt[c] += 1
# print(cnt)
ans = 0
for c in range(20):
    ans = max(ans, cnt[c] * 2 ** c)
print(ans)
