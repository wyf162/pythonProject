# -*- coding: utf-8 -*-
# @Time: 2024/3/27 9:13
# @Author: yfwang
# @File: 1137B.py
# https://codeforces.com/problemset/problem/1137/B
import sys
from math import inf


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

s = input()
t = input()

z = z_function(t)
# print(z)
n = len(z)
mx = 0
for i in range(1, n):
    if n - i == z[i]:
        mx = max(z[i], mx)
# print(mx)
zero = s.count('0')
one = s.count('1')
c0, c1 = t.count('0'), t.count('1')
if c0 <= zero and c1 <= one:
    ans = t
    zero -= c0
    one -= c1

    c0, c1 = t[mx:].count('0'), t[mx:].count('1')
    k = min(zero // c0 if c0 else inf, one // c1 if c1 else inf)
    ans += t[mx:] * k
    zero -= k * c0
    one -= k * c1
    ans += '0' * zero
    ans += '1' * one
    print(ans)
else:
    print(s)
