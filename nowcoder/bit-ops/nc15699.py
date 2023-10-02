# -*- coding : utf-8 -*-
# @Time: 2023/9/25 21:09
# @Author: yefei.wang
# @File: nc15699.py
import math
import sys

BUFSIZE = 8192
MOD = 10 ** 9 + 7
MODD = 998244353
inf = float('inf')
sys.setrecursionlimit(10 ** 6)

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

while True:
    try:
        a, b, c, d = MI()

        y = (b - a + 1) * (d - c + 1)

        if a <= d <= b:
            x = d - max(c, a) + 1
        elif d > b:
            x = b - max(c, a) + 1
        else:
            x = 0
        x = max(x, 0)

        k = math.gcd(x, y)
        x = x // k
        y = y // k
        print(f"{x}/{y}")
    except EOFError:
        break
