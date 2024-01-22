# -*- coding : utf-8 -*-
# @Time: 2024/1/20 20:00
# @Author: yefei.wang
# @File: A.py

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
x, y = 0, 0
for _ in range(n):
    a, b = MI()
    x += a
    y += b

if x>y:
    print('Takahashi')
elif x<y:
    print('Aoki')
else:
    print('Draw')
