# -*- coding : utf-8 -*-
# @Time: 2024/6/8 13:55
# @Author: yefei.wang
# @File: B.py

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

n = I()
points = [LI() for _ in range(n)]
zero = 0

hst = defaultdict(int)
for x, y in points:
    g = math.gcd(x, y)
    if x == 0 and y == 0:
        zero += 1
        continue
    x //= g
    y //= g
    if x <= 0 and y <= 0:
        x *= -1
        y *= -1
    if x <= 0 and y >= 0:
        x *= -1
        y *= -1

    hst[(x, y)] += 1
# print(hst)
print(max(hst.values()) + zero)
