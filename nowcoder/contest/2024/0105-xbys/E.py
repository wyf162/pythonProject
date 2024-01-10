# -*- coding : utf-8 -*-
# @Time: 2024/1/5 23:06
# @Author: yefei.wang
# @File: E.py

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

n, m = MI()
A = LI()
ans = max(max(A), (sum(A) + m - 1) // m)

rst = []
j = 1
t = 0
for i, a in enumerate(A, start=1):
    if t + a <= ans:
        rst.append([i, j, t, t + a])
        t = t + a
    else:
        if ans > t:
            rst.append([i, j, t, ans])
        j += 1
        t = a - (ans - t)
        rst.append([i, j, 0, t])
print(len(rst))
for i in range(len(rst)):
    print(*rst[i])
