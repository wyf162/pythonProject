# -*- coding: utf-8 -*-
# @Time: 2024/5/20 9:33
# @Author: yfwang
# @File: 917A.py
# parenthesis

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())

tcn = 1
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    tot = 0
    for i in range(n):
        a, b = 0, 0
        for j in range(i, n):
            if s[j] == '(':
                a += 1
            elif s[j] == ')':
                a -= 1
            else:
                b += 1
            if a + b < 0:
                break
            if b > a:
                a, b = b, a
            if a == b:
                tot += 1
    print(tot)


