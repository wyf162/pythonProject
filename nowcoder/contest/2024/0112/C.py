# -*- coding : utf-8 -*-
# @Time: 2024/1/12 19:15
# @Author: yefei.wang
# @File: C.py

import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    n = I()
    a = LI()
    b = sorted(a)
    s = b[0] + b[-1]
    ans = True
    for i in range((n + 1) >> 1):
        if b[i] + b[n - 1 - i] != s:
            ans = False
            break
    if not ans:
        print('NO')
        continue
    print('YES')
    ops = []
    hst = defaultdict(list)
    for i, x in enumerate(a):
        hst[x].append(i)

    for i in range(n):
        if a[i] == b[i]:
            heappop(hst[a[i]])
            continue
        l = i
        for r in hst[b[i]]:
            if r > l:
                a[i], a[r] = a[r], a[i]
                heappop(hst[a[i]])

                heappop(hst[a[r]])
                heappush(hst[a[r]], r)
                ops.append([l, r])
                break
    print(len(ops))
    for i in range(len(ops)):
        l, r = ops[i]
        # a[l], a[r] = a[r], a[l]
        print(l + 1, r + 1)
    # print(a == b)
