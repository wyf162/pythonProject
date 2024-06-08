# -*- coding : utf-8 -*-
# @Time: 2024/6/8 13:47
# @Author: yefei.wang
# @File: J.py

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

x1, y1, x2, y2, x3, y3, x4, y4 = MI()
dx1 = x2 - x1
dy1 = y2 - y1
dx2 = x3 - x2
dy2 = y3 - y2
dx3 = x4 - x3
dy3 = y4 - y3
dx4 = x1 - x4
dy4 = y1 - y4

dis = (math.sqrt(dx1 * dx1 + dy1 * dy1) + math.sqrt(dx2 * dx2 + dy2 * dy2) +
       math.sqrt(dx3 * dx3 + dy3 * dy3) + math.sqrt(dx4 * dx4 + dy4 * dy4))
print(dis)
