# -*- coding: utf-8 -*-
# @Time: 2024/2/22 17:15
# @Author: yfwang
# @File: 1907E.py
# https://codeforces.com/problemset/problem/1907/E


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
    n = I()
    cnt = 1
    while n > 0:
        d = n % 10
        n //= 10
        mul = 0
        for i in range(d+1):
            for j in range(d+1):
                if d-i-j>=0:
                    mul += 1
        cnt *= mul
    print(cnt)




