# -*- coding : utf-8 -*-
# @Time: 2024/5/19 19:01
# @Author: yefei.wang
# @File: B.py

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

x = I()

v = int(math.sqrt(x))

c = v + 1
while True:
    if (c * c - x) % 2 == 0:
        ans = (c * c - x) // 2
        break
    else:
        c += 1

c = v
while c >= 0:
    if (x - c * c) % 2 == 0:
        ans = min(ans, (x - c * c) // 2)
        break
    else:
        c -= 1
print(ans)
