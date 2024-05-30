# -*- coding: utf-8 -*-
# @Time: 2024/5/30 16:38
# @Author: yfwang
# @File: abc351E.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 10 ** 18

n = I()
points0 = []
points1 = []
for _ in range(n):
    x, y = MI()
    if (x + y) % 2 == 0:
        points0.append((x, y))
    else:
        points1.append((x, y))


def get_dist(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


def compute(points):
    dis = 0
    m = len(points)
    for i in range(m):
        for j in range(i + 1, m):
            dis += get_dist(points[i], points[j])
    return dis


ans = compute(points0) + compute(points1)
print(ans)
