# -*- coding: utf-8 -*-
# @Time: 2024/4/16 11:11
# @Author: yfwang
# @File: 558C.py
# https://codeforces.com/problemset/problem/558/C


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

n = I()
nums = LI()

cnt = [0] * (10 ** 5 + 1)
for num in nums:
    while num:
        cnt[num] += 1
        num //= 2

ma = max(cnt)
for i in range(10 ** 5, 0, -1):
    if cnt[i] == ma:
        prefix = i
        break

ans = 0
for i in range(n):
    v = nums[i] // prefix
    while True:
        v, resid = divmod(nums[i], prefix)
        if v & -v != v or nums[i] % prefix:
            nums[i] //= 2
            ans += 1
        else:
            break
    nums[i] = nums[i].bit_length()

nums.sort()
print(ans + sum(abs(num - nums[n // 2]) for num in nums))
