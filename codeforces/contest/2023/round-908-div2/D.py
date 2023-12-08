# -*- coding : utf-8 -*-
# @Time: 2023/11/7 23:12
# @Author: yefei.wang
# @File: D.py

import bisect
import sys

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    a = LI()
    b = LI()

    hst = dict()
    for i, x in enumerate(a):
        if x not in hst:
            hst[x] = i

    xs = []
    ixs = []
    for k in sorted(hst.keys()):
        xs.append(k)
        ixs.append(hst[k])

    d = []
    c = [[] for _ in range(n)]
    b.sort()
    for x in b:
        j = bisect.bisect_right(xs, x)
        if j == 0:
            d.append(x)
        else:
            c[ixs[j - 1]].append(x)

    ans = []

    for i in range(n):
        for x in c[i][::-1]:
            ans.append(x)
        ans.append(a[i])
    for x in d[::-1]:
        ans.append(x)
    print(' '.join(map(str, ans)))
