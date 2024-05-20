# -*- coding : utf-8 -*-
# @Time: 2024/5/19 19:21
# @Author: yefei.wang
# @File: E.py

import math
import sys

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
st = {tuple(point) for point in points}
ans = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]

            x4, y4 = x1 + x2 - x3, y1 + y2 - y3
            x5, y5 = x1 + x3 - x2, y1 + y3 - y2
            x6, y6 = x2 + x3 - x1, y2 + y3 - y1
            if (x4, y4) in st or (x5, y5) in st or (x6, y6) in st:
                a = get_dist(*points[i], *points[j])
                b = get_dist(*points[i], *points[k])
                c = get_dist(*points[j], *points[k])
                p = (a + b + c) / 2
                s = 2 * math.sqrt(p * (p - a) * (p - b) * (p - c))
                ans = max(ans, s)
print("%.1f" % ans)
