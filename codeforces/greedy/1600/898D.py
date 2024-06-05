# -*- coding: utf-8 -*-
# @Time: 2024/6/5 9:12
# @Author: yfwang
# @File: 898D.py


import bisect
import sys
from collections import deque

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

tcn = 5
for _tcn_ in range(tcn):
    n, m, k = MI()
    A = LI()
    A.sort()

    ans = 0
    q = deque()
    for i in range(n):
        q.append(i)
        if len(q) == k:
            i1, i2 = q[0], q[-1]
            if A[i2] - A[i1] < m:
                ans += 1
                q.pop()
            else:
                q.popleft()
    print(ans)

