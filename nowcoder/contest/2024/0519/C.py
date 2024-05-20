# -*- coding : utf-8 -*-
# @Time: 2024/5/19 19:09
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

s = input()
n = len(s)

f = [0] * (n + 1)
for i in range(n):
    if 'a' <= s[i] <= 'z':
        f[i + 1] = f[i] + 1
    else:
        f[i + 1] = f[i]

ans = n
for i in range(n - 1):
    ans = min(ans, f[i + 1] + (n - 1 - i - (f[-1] - f[i + 1])))
print(ans)
