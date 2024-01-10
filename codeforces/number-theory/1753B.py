# -*- coding : utf-8 -*-
# @Time: 2024/1/3 21:48
# @Author: yefei.wang
# @File: 1753B.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, x = MI()
a = LI()
c = [0] * (x + 1)
for i in range(n):
    if a[i] == x:
        continue
    c[a[i]] += 1

for i in range(1, x):
    c[i + 1] += c[i] // (i + 1)
    c[i] = c[i] % (i + 1)

if sum(c[:-1]) == 0:
    print('YES')
else:
    print('NO')
