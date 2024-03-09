# -*- coding : utf-8 -*-
# @Time: 2024/3/9 19:59
# @Author: yefei.wang
# @File: A.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353


s = input()
t = ''
n = len(s)
c = 0
for i in range(n):
    if s[i] == '|':
        c ^= 1
    else:
        if c == 1:
            continue
        else:
            t += s[i]
print(t)
