# -*- coding : utf-8 -*-
# @Time: 2023/10/7 20:06
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()

ss = []
for i in range(n):
    ss.append([input().count('o'), i + 1])

ss.sort(key=lambda x: (-x[0], x[1]))

for i in range(n):
    print(ss[i][1], end=' ')
print()