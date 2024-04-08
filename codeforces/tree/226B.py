# -*- coding: utf-8 -*-
# @Time: 2024/4/8 9:59
# @Author: yfwang
# @File: 226B.py
# https://codeforces.com/problemset/problem/226/B

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

n = I()
nums = LI()
nums.sort(reverse=True)
acc = list(accumulate(nums, initial=0))
# print(acc)

ans = [0] * (n + 1)
for i in range(1, n+1):
    pt = 1
    cur = i
    weight = 1
    while pt < n:
        ans[i] += (acc[min(pt+cur, n)] - acc[pt]) * weight
        pt += cur
        cur *= i
        weight += 1
q = I()
ks = LI()
ret = [ans[min(k, n)] for k in ks]
print(' '.join(str(x) for x in ret))
