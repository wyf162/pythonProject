# -*- coding: utf-8 -*-
# @Time: 2024/3/18 14:20
# @Author: yfwang
# @File: 1793D.py
# https://codeforces.com/problemset/problem/1793/D
# mex permutation

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
p1 = LGMI()
p2 = LGMI()
ind1 = [0] * n
ind2 = [0] * n
for i in range(n):
    ind1[p1[i]] = i
    ind2[p2[i]] = i


def check(length):
    return length * (length + 1) // 2


ans = 1
x = min(ind1[0], ind2[0])
y = max(ind1[0], ind2[0])
ans += check(x) + check(n - y - 1) + check(y - x - 1)

for i in range(1, n):
    a = min(ind1[i], ind2[i])
    b = max(ind1[i], ind2[i])

    if b < x:
        ans += (x - b) * (n - y)
    elif y < a:
        ans += (x + 1) * (a - y)
    elif a < x < y < b:
        ans += (x - a) * (b - y)

    x = min(x, a)
    y = max(y, b)
print(ans)
