# -*- coding : utf-8 -*-
# @Time: 2024/6/8 13:53
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

n, m = MI()
A = LI()
B = LI()
i = 0
j = 0
ans = 0
while i < n and j < m:
    if A[i] <= B[j]:
        ans += B[j]
        i += 1
        j += 1
    else:
        j += 1
print(ans)
