# -*- coding : utf-8 -*-
# @Time: 2024/6/14 19:14
# @Author: yefei.wang
# @File: B.py

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

n = I()
s = input()

c0 = s.count('0')
c1 = n - c0
if c0 == 0 or c1 == 0:
    print(0)
elif c0 == 1 and c1 == 1:
    print(-1)
elif c0 == c1:
    print(2)
else:
    print(1)
