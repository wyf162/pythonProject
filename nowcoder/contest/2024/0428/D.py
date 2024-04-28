# -*- coding : utf-8 -*-
# @Time: 2024/4/28 20:27
# @Author: yefei.wang
# @File: D.py

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

tot = 0
diff = 0
s = sum(nums) * 2
for i in range(n):
    tot += i * i * nums[i]
    diff += (1 - 2 * i) * nums[i]

ans = tot
for i in range(1, n):
    tot += diff
    diff += s
    ans = min(ans, tot)

print(ans)
