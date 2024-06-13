# -*- coding: utf-8 -*-
# @Time: 2024/6/13 9:05
# @Author: yfwang
# @File: 1237D.py
# 单调队列

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

tcn = 3
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    ans = [-1] * n
    nums = nums + nums + nums
    q = deque()

    j = 0
    for i in range(n):
        while j < n * 3 and (not q or  nums[j] * 2 >= nums[q[0]]):
            while q and nums[q[-1]] <= nums[j]:
                q.pop()
            q.append(j)
            j += 1
        if j == n * 3:
            ans[i] = -1
        else:
            ans[i] = j - i
        if q[0] == i:
            q.popleft()

    print(*ans)













