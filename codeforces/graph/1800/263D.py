# -*- coding : utf-8 -*-
# @Time: 2024/6/9 14:09
# @Author: yefei.wang
# @File: 263D.py
# cycle dfs

import sys

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

tcn = 1
for _tcn_ in range(tcn):
    n, m, k = MI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    parent = [-1] * n
    time = [0] * n
    time[0] = 1
    x = 0
    ans = []
    while True:
        for y in g[x]:
            if time[y]:
                if time[x] - time[y] >= k:
                    while x != y:
                        ans.append(x)
                        x = parent[x]
                    ans.append(y)
                    break
                continue
            parent[y] = x
            time[y] = time[x] + 1
            x = y
            break
        if ans:
            break

    print(len(ans))
    print(' '.join(str(x+1) for x in ans))