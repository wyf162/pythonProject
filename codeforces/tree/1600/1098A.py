# -*- coding: utf-8 -*-
# @Time: 2024/6/5 16:30
# @Author: yfwang
# @File: 1098A.py
# trees

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
inf = 10 ** 18

tcn = 4
for _tcn_ in range(tcn):
    n = I()
    father = LGMI()
    tree = [[] for _ in range(n)]
    for i, fa in enumerate(father, start=1):
        tree[fa].append(i)
    father.insert(0, -1)
    acc = LI()
    depth = [0] * n
    A = [0] * n
    depth[0] = 1
    A[0] = acc[0]

    stk = [0]
    while stk:
        x = stk.pop()

        for y in tree[x]:
            if acc[y] == -1:
                mi = inf
                for ny in tree[y]:
                    mi = min(mi, acc[ny])
                if mi == inf:
                    A[y] = 0
                else:
                    A[y] = mi - acc[x]
                acc[y] = acc[x] + A[y]
            else:
                A[y] = acc[y] - acc[x]
            depth[y] = depth[x] + 1
            stk.append(y)
    # print(tree)
    # print(depth)
    # print(A)
    if any(x < 0 for x in A):
        print(-1)
    else:
        print(sum(A))
