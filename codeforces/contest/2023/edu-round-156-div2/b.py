# -*- coding : utf-8 -*-
# @Time: 2023/10/9 22:51
# @Author: yefei.wang
# @File: c.py
import math
import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()


def calc_dist(a, b, c, d):
    return math.sqrt((a - c) * (a - c) + (b - d) * (b - d))


def check(w):
    d = calc_dist(x1, y1, x2, y2)
    d1 = calc_dist(x1, y1, 0, 0)
    d2 = calc_dist(x2, y2, 0, 0)
    h1 = calc_dist(x1, y1, x, y)
    h2 = calc_dist(x2, y2, x, y)
    if d1 <= w and h1 <= w:
        return True
    elif d2 <= w and h2 <= w:
        return True
    elif d <= 2 * w and (d1 <= w or d2 <= w) and (h1 <= w or h2 <= w):
        return True
    else:
        return False


for _tcn_ in range(tcn):
    x, y = MI()
    x1, y1 = MI()
    x2, y2 = MI()
    l, r = 0, 10 ** 4
    ans = r
    decision = 1e-12
    while r - l >= decision * 2:
        m = (r + l) / 2
        # print(l, m, r)
        if check(m):
            ans = m
            r = m - decision
        else:
            l = m + decision
    print(ans)
