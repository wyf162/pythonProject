# -*- coding: utf-8 -*-
# @Time: 2024/4/26 10:10
# @Author: yfwang
# @File: 1525E.py
# https://codeforces.com/problemset/problem/1525/E


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

n, m = MI()

