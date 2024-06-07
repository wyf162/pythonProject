# -*- coding: utf-8 -*-
# @Time: 2024/4/29 15:06
# @Author: yfwang
# @File: 1525C.py
# https://codeforces.com/contest/1525/problem/C

import sys
from collections import deque

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
    nums = LI()
    dirs = input().split()

    dd = []
    for i in range(n):
        dd.append((nums[i], i))
    dd.sort()
    cnv = [0] * n
    ind = [0] * n
    for i in range(n):
        j = dd[i][1]
        cnv[i] = j
        ind[j] = i

    nums = [nums[cnv[i]] for i in range(n)]
    dirs = [dirs[cnv[i]] for i in range(n)]
    # print(nums)
    # print(dirs)
    # print(cnv)

    idx1, idx2 = [], []
    for i, num in enumerate(nums):
        if num % 2:
            idx1.append(i)
        else:
            idx2.append(i)

    rets = [-1] * n

    stkL = deque()
    stkR = deque()
    for i in idx1:
        if dirs[i] == 'R':
            stkR.append(i)
        elif dirs[i] == 'L':
            if stkR:
                j = stkR.pop()
                t = (nums[i] - nums[j]) // 2
                rets[i] = rets[j] = t
            else:
                stkL.append(i)
    while len(stkL) >= 2:
        i1, i2 = stkL.popleft(), stkL.popleft()
        t = (nums[i1] + nums[i2]) // 2
        rets[i1] = rets[i2] = t

    while len(stkR) >= 2:
        i1, i2 = stkR.pop(), stkR.pop()
        t = (2 * m - nums[i1] - nums[i2]) // 2
        rets[i1] = rets[i2] = t

    if stkL and stkR:
        i1, i2 = stkL.pop(), stkR.pop()
        t = (nums[i1] + m - nums[i2] + m) // 2
        rets[i1] = rets[i2] = t

    stkL = deque()
    stkR = deque()
    for i in idx2:
        if dirs[i] == 'R':
            stkR.append(i)
        elif dirs[i] == 'L':
            if stkR:
                j = stkR.pop()
                t = (nums[i] - nums[j]) // 2
                rets[i] = rets[j] = t
            else:
                stkL.append(i)
    while len(stkL) >= 2:
        i1, i2 = stkL.popleft(), stkL.popleft()
        t = (nums[i1] + nums[i2]) // 2
        rets[i1] = rets[i2] = t

    while len(stkR) >= 2:
        i1, i2 = stkR.pop(), stkR.pop()
        t = (2 * m - nums[i1] - nums[i2]) // 2
        rets[i1] = rets[i2] = t

    if stkL and stkR:
        i1, i2 = stkL.pop(), stkR.pop()
        t = (nums[i1] + m - nums[i2] + m) // 2
        rets[i1] = rets[i2] = t

    rets = [rets[ind[i]] for i in range(n)]
    print(*rets)
