# -*- coding : utf-8 -*-
# @Time: 2024/5/19 19:15
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

n, k = MI()
nums = LI()

st = dict()
for i in range(k):
    if 1 <= nums[i] <= k:
        if nums[i] not in st:
            st[nums[i]] = 1
        else:
            st[nums[i]] += 1

ans = 0
if len(st) == k:
    ans += 1

for i in range(k, n):
    if 1 <= nums[i] <= k:
        if nums[i] not in st:
            st[nums[i]] = 1
        else:
            st[nums[i]] += 1

    if 1 <= nums[i - k] <= k:
        st[nums[i - k]] -= 1
        if st[nums[i - k]] == 0:
            del st[nums[i - k]]
    if len(st) == k:
        ans += 1
print(ans)
