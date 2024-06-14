# -*- coding : utf-8 -*-
# @Time: 2024/6/14 19:12
# @Author: yefei.wang
# @File: A.py

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

s1 = input()
s2 = input()
n1, n2 = len(s1), len(s2)


if n1 == 6 or n2 == 6:
    print(-1)
else:
    print(abs(n1 - n2) + 1)
