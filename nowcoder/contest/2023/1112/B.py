# -*- coding : utf-8 -*-
# @Time: 2023/11/12 19:41
# @Author: yefei.wang
# @File: B.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

a, b, x, y = MI()
ans = 21
for i in range(21):
    na = a- y * i
    nb = b - y * i
    tmp = i
    if na > 0:
        tmp += (na + x - 1) // x
    if nb > 0:
        tmp += (nb + x - 1) // x
    ans = min(ans, tmp)

print(ans)
