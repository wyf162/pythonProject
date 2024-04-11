# -*- coding: utf-8 -*-
# @Time: 2024/4/11 9:05
# @Author: yfwang
# @File: 296B.py
# https://codeforces.com/problemset/problem/296/B

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

n = I()
s1 = input()
s2 = input()

# 45, 10, 45
x00 = 1
x10 = 0
x01 = 0
x11 = 0

for i in range(n):
    if s1[i] == '?' and s2[i] == '?':
        x11 = x11 * 100 + x10 * 45 + x01 * 45
        x10 = x00 * 45 + x10 * 55
        x01 = x00 * 45 + x01 * 55
        x00 = x00 * 10

    elif s1[i] == '?' and s2[i] != '?':
        a, b = int(s2[i]), 9 - int(s2[i])
        x11 = x11 * 10 + x10 * a + x01 * b
        x10 = x00 * b + x10 * (b + 1)
        x01 = x00 * a + x01 * (a + 1)
        x00 = x00 * 1

    elif s1[i] != '?' and s2[i] == '?':
        a, b = int(s1[i]), 9 - int(s1[i])
        x11 = x11 * 10 + x10 * b + x01 * a
        x10 = x00 * a + x10 * (a + 1)
        x01 = x00 * b + x01 * (b + 1)
        x00 = x00 * 1

    else:
        if s1[i] > s2[i]:
            x11 = x11 + x01
            x10 = x00 + x10
            x00 = 0
            x01 = 0
        elif s1[i] < s2[i]:
            x11 = x11 + x10
            x01 = x00 + x01
            x00 = 0
            x10 = 0
    x00 %= mod
    x10 %= mod
    x01 %= mod
    x11 %= mod
print(x11)
