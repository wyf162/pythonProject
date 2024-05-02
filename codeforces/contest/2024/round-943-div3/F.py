# -*- coding : utf-8 -*-
# @Time: 2024/5/3 0:04
# @Author: yefei.wang
# @File: F.py

import sys
from collections import defaultdict
import bisect

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
    n, q = MI()
    A = LI()
    queries = [LI() for _ in range(q)]

    hst = defaultdict(list)
    pre_xor = [0] * (n + 1)
    for i in range(n):
        pre_xor[i + 1] = pre_xor[i] ^ A[i]
        hst[pre_xor[i + 1]].append(i)

    for query in queries:
        l, r = query
        t = pre_xor[r] ^ pre_xor[l - 1]
        ans = False
        if t == 0:
            ans = True
        else:
            t0 = pre_xor[l - 1]
            t1 = t0 ^ t
            i1 = bisect.bisect_left(hst[t1], l - 1)
            if i1 < len(hst[t1]):
                i2 = bisect.bisect_left(hst[t0], hst[t1][i1] + 1)
                if i2 < len(hst[t0]) and hst[t0][i2] < r:
                    ans = True
                    # print(hst[t1][i1] + 1, hst[t0][i2] + 1)
        YN(ans)
    # print()
