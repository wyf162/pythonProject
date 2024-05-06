# -*- coding: utf-8 -*-
# @Time: 2024/5/6 9:31
# @Author: yfwang
# @File: 1759D.py
# https://codeforces.com/problemset/problem/1759/D

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../output.txt', 'w')
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
    n, m = MI()
    two = 0
    five = 0
    x = n
    while x % 2 == 0:
        x = x // 2
        two += 1
    while x % 5 == 0:
        five += 1
        x = x // 5

    if two <= five:
        five -= two
        two = 0
    else:
        two -= five
        five = 0

    if two:
        y = 1
        while two and y * 5 <= m:
            two -= 1
            y *= 5
    elif five:
        y = 1
        while five and y * 2 <= m:
            five -= 1
            y *= 2
    else:
        y = 1
    k = m // y * y
    while y * 10 <= m:
        y = y * 10
        k = m // y * y
    print(n * k)





















