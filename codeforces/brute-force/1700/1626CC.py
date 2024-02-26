# -*- coding : utf-8 -*-
# @Time: 2023/10/17 22:32
# @Author: yefei.wang
# @File: 1626C.py

import sys

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    k = LI()
    h = LI()
    b = []
    e = []
    for i in range(n):
        if b and b[-1] >= k[i]-h[i]:
            while b and b[-1] >= k[i] - h[i]:
                b.pop()
                e.pop()
            b.append(k[i] - h[i])
            e.append(k[i])
        elif b and b[-1] < k[i] - h[i] < e[-1]:
            e[-1] = k[i]
        else:
            b.append(k[i] - h[i])
            e.append(k[i])

    ans = 0
    for x, y in zip(b, e):
        ans += (y - x) * (y - x + 1) // 2
    print(ans)