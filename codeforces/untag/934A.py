# -*- coding : utf-8 -*-
# @Time: 2024/2/19 19:52
# @Author: yefei.wang
# @File: 934A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
a = LI()
b = LI()
a.sort()
b.sort()

print(min(max(a[1] * b[0], a[1] * b[-1], a[-1] * b[0], a[-1] * b[-1]),
          max(a[0] * b[0], a[0] * b[-1], a[-2] * b[0], a[-2] * b[-1])))
