# -*- coding: utf-8 -*-
# @Time: 2024/6/5 14:32
# @Author: yfwang
# @File: 576B.py
# graphs trees

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 2
for _tcn_ in range(tcn):
    n = I()
    A = LGMI()
    g = [[] for _ in range(n)]
    invariant_point = -1
    for i, x in enumerate(A):
        g[i].append(x)
        g[x].append(i)
        if i == x:
            invariant_point = i
            break
    if invariant_point >= 0:
        YN(True)
        for i in range(n):
            if i != invariant_point:
                print(i + 1, invariant_point + 1)
        continue

    colors = [0] * n
    color = 0
    ans = True
    for i in range(n):
        if colors[i] != 0:
            continue
        color += 1
        cnt = 0
        q = [i]
        while q:
            x = q.pop()
            if colors[x] == 0:
                colors[x] = color
                cnt += 1
            for y in g[x]:
                if colors[y] == 0:
                    colors[y] = -colors[x]
                    cnt += 1
                    q.append(y)
                else:
                    if colors[y] == -colors[x]:
                        continue
                    else:
                        break
        if cnt % 2:
            ans = False
            break

    if ans is False:
        YN(ans)
        continue

    invariant_edge = [-1, -1]
    odd = []
    event = []
    hst = Counter()
    for i, color in enumerate(colors):
        if color < 0:
            odd.append(i)
        else:
            event.append(i)
        hst[abs(color)] += 1

    for k, v in hst.items():
        if v == 2:
            invariant_edge = colors.index(-k), colors.index(k)
            break
    else:
        YN(False)
        continue

    YN(True)
    print(invariant_edge[0] + 1, invariant_edge[1] + 1)
    for x in odd:
        if x == invariant_edge[0]:
            continue
        print(invariant_edge[1] + 1, x + 1)
    for x in event:
        if x == invariant_edge[1]:
            continue
        print(invariant_edge[0] + 1, x + 1)
