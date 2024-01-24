# -*- coding : utf-8 -*-
# @Time: 2024/1/24 21:32
# @Author: yefei.wang
# @File: 1481C.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    a = LI()
    b = LI()
    c = LI()
    hst = [[] for _ in range(n + 1)]
    last = -1
    for i in range(n):
        if b[i] == c[-1]:
            last = i + 1
        if a[i] == b[i]:
            continue
        else:
            hst[b[i]].append(i + 1)
    if last < 0:
        print('NO')
        continue
    if hst[c[-1]]:
        last = hst[c[-1]][0]
    ans = []
    for x in c:
        if hst[x]:
            i = hst[x].pop()
            ans.append(i)
        else:
            ans.append(last)
    if any(x for x in hst):
        print('NO')
    else:
        print('YES')
        print(*ans)
        # for i1, x in enumerate(ans):
        #     a[x - 1] = c[i1]
        #
        # print(a == b)
        # print(*a)
        # print(*b)
        # print(b)
