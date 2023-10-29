# -*- coding : utf-8 -*-
# @Time: 2023/10/28 21:10
# @Author: yefei.wang
# @File: c.py

import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, m = MI()
a = LI()
a.sort()
i, j = 0, 0
ans = 1
while j < n:
    while j < n and a[j] - a[i] < m:
        j += 1
    ans = max(ans, j - i)
    i += 1

print(ans)
