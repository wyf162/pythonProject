# -*- coding : utf-8 -*-
# @Time: 2024/1/28 19:19
# @Author: yefei.wang
# @File: C.py

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

s = list(input())
c = dict()
n = len(s)
for i in range(n//2):
    c[s[i]] = i
    if len(c) >= 2:
        k1, k2 = list(c.keys())
        i1, i2 = c[k1], c[k2]
        s[i1], s[i2] = s[i2], s[i1]
        s[-i1-1], s[-i2-1] = s[-i2-1], s[-i1-1]
        print(''.join(s))
        break
else:
    print(-1)
