# -*- coding: utf-8 -*-
# @Time: 2024/6/24 9:30
# @Author: yfwang
# @File: 336C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
A = LI()
ans = []
for v in range(31, -1, -1):
    ans = []
    x = (1 << (v + 1)) - 1
    for a in A:
        if a >> v & 1 == 0:
            continue
        x = x & a
        ans.append(a)
    if x == (1 << v):
        break

print(len(ans))
print(*ans)