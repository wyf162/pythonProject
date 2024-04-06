# -*- coding : utf-8 -*-
# @Time: 2024/4/6 20:01
# @Author: yefei.wang
# @File: B.py

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

n = I()
points = [LI() for _ in range(n)]
ans = [0] * n
for i in range(n):
    dist = 0
    for j in range(n):
        x = points[i][0] - points[j][0]
        y = points[i][1] - points[j][1]
        tmp = x * x + y * y
        if tmp > dist:
            dist = tmp
            ans[i] = j + 1
print(*ans)
