# -*- coding : utf-8 -*-
# @Time: 2023/12/2 20:04
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('./../../input.txt')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, S, M, L = MI()
ans = N * S

n1 = (N + 5) // 6
n2 = (N + 7) // 8
for i in range(n1 + 1):
    for j in range(n2 + 1):
        k = (N - 6 * i - 8 * j + 11) // 12
        k = max(k, 0)
        tmp = i * S + j * M + k * L
        ans = min(ans, tmp)
print(ans)