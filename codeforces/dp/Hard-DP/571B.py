# -*- coding: utf-8 -*-
# @Time: 2024/3/20 12:59
# @Author: yfwang
# @File: 571B.py

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

n, k = map(int, input().split())

v = list(map(int, input().split()))
v.sort()
v = [0] + v


# k 个子数组，b 个子数组长度为 a+1，k - b 个子数组为 a
a, b = divmod(n, k)

# 前 k 个子数组，选了 j 个长度为 a+1 的子数组
f = [[10 ** 18] * (b + 1) for _ in range(k + 1)]

f[0][0] = 0
for i in range(1, k + 1):
    for j in range(min(i + 1, b + 1)):
        if i - j > k - b:
            continue
        # 最后选的长度为只能 a
        if j == 0:
            f[i][j] = f[i - 1][j] + v[i * a] - v[(i - 1) * a + 1]
        # 最后选的长度可以为 a 或者 a+1
        else:
            f[i][j] = min(f[i - 1][j] + v[i * a + j] - v[i * a + j - a + 1],
                          f[i - 1][j - 1] + v[i * a + j] - v[i * a + j - (a + 1) + 1])

print(f[k][b])
