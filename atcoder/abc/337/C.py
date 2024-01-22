# -*- coding : utf-8 -*-
# @Time: 2024/1/20 20:08
# @Author: yefei.wang
# @File: C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
a = LI()
b = [0] * (n+1)
c = []
for i, pre in enumerate(a, start=1):
    if pre == -1:
        c.append(i)
    else:
        b[pre] = i

for _ in range(n-1):
    c.append(b[c[-1]])
print(*c)



