# -*- coding : utf-8 -*-
# @Time: 2023/10/14 10:44
# @Author: yefei.wang
# @File: 1625C.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, l, K = MI()
d = LI()
a = LI()
d.append(l)

f = [[0x3f3f3f3f for j in range(K+1)] for i in range(n+1)]
f[0][0] = 0
for i in range(1, n+1):
    f[i][0] = f[i-1][0] + a[i-1] * (d[i] - d[i-1])

# for i in range(1, n+1):
#     print(f[i][0], end=' ')
# print()


for i in range(1, n+1):
    for j in range(i):
        dk = i - j - 1
        for k in range(dk, K+1):
            f[i][k] = min(f[i][k], f[j][k-dk] + a[j] * (d[i] - d[j]))

ans = min(f[n])
print(ans)
