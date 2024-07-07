# -*- coding : utf-8 -*-
# @Time: 2024/7/7 10:04
# @Author: yefei.wang
# @File: 1920D.py

import bisect
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
inf = 1 << 64

tcn = I()
for _tcn_ in range(tcn):
    n, q = MI()
    end_points = dict()
    cur = 0
    nums = []
    lens = []
    for _ in range(n):
        typ, x = MI()
        if cur > inf:
            continue
        if typ == 1:
            end_points[cur] = x
            cur += 1
            nums.append(cur)
            lens.append(cur)
        elif typ == 2:
            lens.append(cur)
            cur += cur * x
            nums.append(cur)

    queries = LGMI()
    ans = [0] * q
    for i in range(q):
        x = queries[i]
        while True:
            if x in end_points:
                ans[i] = end_points[x]
                break
            else:
                j = bisect.bisect_left(nums, x)
                x = x % lens[j]
    print(*ans)
