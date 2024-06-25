# -*- coding: utf-8 -*-
# @Time: 2024/6/25 13:08
# @Author: yfwang
# @File: 1032D.py

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


def dis(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5


def find_points(x, y):
    if a:
        yield -(b * y + c) / a, y
    if b:
        yield x, -(a * x + c) / b


a, b, c = MI()
x1, y1, x2, y2 = MI()

ans = abs(x1 - x2) + abs(y1 - y2)
for pt1 in find_points(x1, y1):
    for pt2 in find_points(x2, y2):
        ans = min(ans, dis((x1, y1), pt1) + dis(pt1, pt2) + dis(pt2, (x2, y2)))

print(ans)
