# -*- coding : utf-8 -*-
# @Time: 2024/6/5 23:01
# @Author: yefei.wang
# @File: A.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
inf = 0x3f3f3f3f

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums1 = LI()
    nums2 = LI()
    g1 = [[] for _ in range(n)]
    g2 = [[] for _ in range(n)]
    in_deg = [0] * n
    out_deg = [0] * n
    for i in range(1, n):
        if nums1[i - 1] + nums2[i - 1] >= nums1[i]:
            g1[i - 1].append(i)
            in_deg[i] += 1
            out_deg[i-1] += 1
        if nums1[i] - nums2[i] <= nums1[i-1]:
            g2[i].append(i - 1)
            in_deg[i - 1] += 1
            out_deg[i] += 1
    if in_deg.count(0) > 2:
        YN(False)
    elif in_deg.count(0) < 2:
        YN(True)
    else:
        vis = [[] for _ in range(n)]
        zeros = []
        for i, d in enumerate(in_deg):
            if d == 0:
                zeros.append(i)

        for x in zeros:
            stk = [x]
            while stk:
                x = stk.pop()
                for y in g1[x]:
                    stk.append(y)
                    vis[y].append((x, 1))

        for x in zeros:
            stk = [x]
            while stk:
                x = stk.pop()
                for y in g2[x]:
                    stk.append(y)
                    vis[y].append((x, 2))

        hst = dict()
        ans = True
        for x in range(n):
            if len(vis[x]) == 1:
                start, dire = vis[x][0]
                hst[start] = dire

        unvis = [0] * n
        for x in zeros:
            if x in hst:
                if hst[x] == 1:
                    stk = [x]
                    while stk:
                        x = stk.pop()
                        unvis[x] = 1
                        for y in g1[x]:
                            stk.append(y)
                elif hst[x] == 2:
                    stk = [x]
                    while stk:
                        x = stk.pop()
                        unvis[x] = 1
                        for y in g2[x]:
                            stk.append(y)
            else:
                stk = [x]
                while stk:
                    x = stk.pop()
                    unvis[x] = 1
                    for y in g1[x]:
                        stk.append(y)
        if any(unvis[x]==0 for x in range(n)):
            YN(False)
        else:
            YN(True)