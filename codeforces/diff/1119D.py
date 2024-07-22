# -*- coding: utf-8 -*-
# @Time: 2024/7/22 9:43
# @Author: yfwang
# @File: 1119D.py

import bisect
import sys
from itertools import accumulate

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

n = I()
nums = LI()
q = I()
queries = []
for i in range(q):
    x1, x2 = MI()
    queries.append(x2 - x1 + 1)

nums.sort()
vals = [nums[i + 1] - nums[i] for i in range(n - 1)]
vals.append(10 ** 18 + 1)
vals.sort()

acc = list(accumulate(vals, initial=0))

outs = []
for x in queries:
    p = bisect.bisect_right(vals, x)
    outs.append(acc[p] + (n - p) * x)

print(' '.join(str(x) for x in outs))
