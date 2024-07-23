# -*- coding: utf-8 -*-
# @Time: 2024/7/23 11:19
# @Author: yfwang
# @File: 792D.py

import sys

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

n, q = MI()


def get_unit(x):
    b = ret = 1
    while b <= x:
        if x % b == 0:
            ret = b
            b *= 2
        else:
            break
    return ret


for _ in range(q):
    x = I()
    path = input()
    for c in path:
        d = get_unit(x)
        if c == 'U':
            x1, x2 = x + d, x - d
            if x1 % (d * 4):
                x = x1
            else:
                x = x2
            if x == 0:
                x += d
            if x > n:
                x -= d
        elif c == 'L':
            x -= d // 2
            if x < 1:
                x += d // 2
        elif c == 'R':
            x += d // 2
            if x > n:
                x -= d // 2
    print(x)
