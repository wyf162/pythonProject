# -*- coding: utf-8 -*-
# @Time: 2024/4/29 9:03
# @Author: yfwang
# @File: 1365C.py
# https://codeforces.com/problemset/problem/1365/C

import sys
from collections import Counter

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
A = LGMI()
B = LGMI()
ind = [0] * n
for i, a in enumerate(A):
    ind[a] = i

cnt = Counter()
for i, b in enumerate(B):
    cnt[ind[b] - i] += 1
    cnt[ind[b] - i + n] += 1
ans = max(cnt.values())
print(cnt)
print(ans)
