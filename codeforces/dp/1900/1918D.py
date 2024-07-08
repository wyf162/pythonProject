# -*- coding: utf-8 -*-
# @Time: 2024/7/8 15:54
# @Author: yfwang
# @File: 1918D.py
# https://codeforces.com/contest/1918/problem/D
# mono_queue

import sys
from collections import deque
from itertools import accumulate
# from heapq import heappop, heappush

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
inf = 10 ** 15

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    A = LI()
    PA = list(accumulate(A, initial=0))

    L, R = 1, inf
    while L <= R:
        ans = False
        mid = (L + R) // 2
        i1 = 0
        # h = [(0, 0)]
        mono_queue = deque()
        mono_queue.append((0, 0))
        for i in range(n):
            while PA[i] - PA[i1] > mid:
                i1 += 1
            # while h[0][1] < i1:
            #     heappop(h)
            # mi = h[0][0]
            while mono_queue[0][1] < i1:
                mono_queue.popleft()
            mi = mono_queue[0][0]
            # heappush(h, (mi + A[i], i + 1))
            while mono_queue and mono_queue[-1][0] >= mi + A[i]:
                mono_queue.pop()
            mono_queue.append((mi+A[i], i+1))

            if A[i] + mi <= mid and PA[-1] - (PA[i + 1]) <= mid:
                ans = True
                break
        if ans:
            ret = mid
            R = mid - 1
        else:
            L = mid + 1

    print(ret)
