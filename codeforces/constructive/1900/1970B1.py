# -*- coding : utf-8 -*-
# @Time: 2024/6/22 16:11
# @Author: yefei.wang
# @File: 1970B1.py
# https://codeforces.com/problemset/problem/1970/B1

import sys
from collections import Counter

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
A = LI()
cnt = Counter(A)
if 0 not in cnt and max(cnt.values()) == 1:
    print('NO')
    exit()

f = [0] * n
h = [0] * n
ai = [(a, i) for i, a in enumerate(A)]
ai.sort()

for i in range(1, n):
    a = ai[i][0]
    if a == 0:
        h[i] = 0
        f[i] = i
    else:
        if i <= a < 2 * n:
            h[i] = a - i
            f[i] = 0
        elif a < i:
            h[i] = h[i - a]
            f[i] = i - a
if ai[0][0] != 0:
    f[0] = 1

coords = [None for _ in range(n)]
friends = [None for _ in range(n)]
for i in range(n):
    j = ai[i][1]
    coords[j] = [i + 1, h[i] + 1]
    friends[j] = ai[f[i]][1] + 1

print('YES')
for x, y in coords:
    print(x, y)
print(*friends)
