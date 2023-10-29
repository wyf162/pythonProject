# -*- coding : utf-8 -*-
# @Time: 2023/10/10 22:20
# @Author: yefei.wang
# @File: 394B.py

import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
mi = min(a)
v = 1
for i, x in enumerate(a):
    if x == mi:
        v = i + 1

x, y = divmod(n, mi)
cnt = {v: x}
for i in range(8, v - 1, -1):
    d = a[i] - mi
    if y >= d:
        cnt[i + 1] = min(y // d, cnt[v])
        cnt[v] -= cnt[i + 1]
        y %= d
ans = ''
for i in range(9, 0, -1):
    if i in cnt:
        ans += str(i) * cnt[i]

if ans:
    print(ans)
else:
    print(-1)
