# -*- coding: utf-8 -*-
# @Time: 2024/4/18 10:42
# @Author: yfwang
# @File: 1310A.py
# https://codeforces.com/problemset/problem/1310/A

import sys
from heapq import heappop, heappush

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

n = I()
A = LI()
T = LI()

h = []
tot = 0
last_t = 0
ans = 0
for i in sorted(range(n), key=lambda x: A[x]):
    for _ in range(A[i] - last_t):
        if h:
            tot += heappop(h)
            ans += tot
        else:
            break
    heappush(h, -T[i])
    tot += T[i]
    last_t = A[i]

while h:
    tot += heappop(h)
    ans += tot

print(ans)
