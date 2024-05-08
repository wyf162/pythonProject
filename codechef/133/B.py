# -*- coding : utf-8 -*-
# @Time: 2024/5/8 22:33
# @Author: yefei.wang
# @File: B.py

import math
import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    N = I()
    A = LI()
    B = list(sorted(math.log(x) for x in A))
    ans = 0
    for i in range(N):
        j = bisect.bisect_right(B, math.log(A[i]) / (i + 1))
        ans += j
    print(ans)
