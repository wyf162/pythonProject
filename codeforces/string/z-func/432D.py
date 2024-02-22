# -*- coding: utf-8 -*-
# @Time: 2024/2/22 9:17
# @Author: yfwang
# @File: 432D.py
# https://codeforces.com/problemset/problem/432/D

import sys

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


def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    z[0] = n
    return z


ss = list(input())
n = len(ss)
z = z_function(ss)
cnt = [0] * (n + 1)

for i in range(n):
    cnt[z[i]] += 1

for i in range(n-1, -1, -1):
    cnt[i] += cnt[i+1]

res = []
for i in range(n):
    if i + z[i] == n:
        res.append([z[i], cnt[z[i]]])

res.reverse()
print(len(res))
for x in res:
    print(*x)
