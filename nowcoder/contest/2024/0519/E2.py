# -*- coding : utf-8 -*-
# @Time: 2024/5/19 20:40
# @Author: yefei.wang
# @File: E2.py

import math
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


def get_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


n = I()
points = [LI() for _ in range(n)]
groups = defaultdict(list)
ans = -1

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        groups[(x1 + x2, y1 + y2)].append((i, j))

for _, group in groups.items():
    m = len(group)
    for j1 in range(m):
        for j2 in range(j1 + 1, m):
            i1, i2 = group[j1]
            i3, i4 = group[j2]
            if i1 == i3 or i1 == i4 or i2 == i3 or i2 == i4:
                continue


print("%.1f" % ans)
