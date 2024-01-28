# -*- coding : utf-8 -*-
# @Time: 2024/1/28 19:15
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

s = list(input())
s.sort()
for i in range(1, 10):
    i = str(i)
    if i in s:
        s.pop(s.index(i))
        s.insert(0, i)
        break
print(''.join(s))
