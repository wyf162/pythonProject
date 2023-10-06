# -*- coding : utf-8 -*-
# @Time: 2023/10/5 2:26
# @Author: yefei.wang
# @File: P1080.py

import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a, b = MI()
c = [LI() for _ in range(n)]
c.sort(key=lambda x: (x[1] * x[0]))
l = a
ans = 0
for i in range(n):
    ans = max(ans, l // c[i][1])
    l *= c[i][0]
print(ans)
