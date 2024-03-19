# -*- coding: utf-8 -*-
# @Time: 2024/3/19 15:13
# @Author: yfwang
# @File: 1728D.py
# https://codeforces.com/problemset/problem/1728/D


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

tcn = I()
for _tcn_ in range(tcn):
    s = input()

    flag = 0
    n = len(s)
    p = n
    for i in range(n):
        if s[i] != s[n - i - 1]:
            p = i
            break
    for i in range(p, n - p, 2):
        if s[i] != s[i + 1]:
            flag = 1
    if flag == 1:
        print('Alice')
    else:
        print('Draw')
