# -*- coding : utf-8 -*-
# @Time: 2024/5/1 23:10
# @Author: yefei.wang
# @File: D.py

import sys

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
    n = I()
    nums = LI()
    q = I()
    queries = [LI() for _ in range(q)]
    one = [0] * (n + 1)
    two = [0] * (n + 1)
    for i, x in enumerate(nums):
        one[i + 1] = one[i] + int(x == 1)
        two[i + 1] = two[i] + int(x == 2)

    for L, R, K in queries:
        c = R - L + 1
        c1 = one[R] - one[L - 1]
        c2 = two[R] - two[L - 1]
        # 不妨设 c1 <= c2
        if c1 > c2:
            c1, c2 = c2, c1

        # 不妨设 x1 <= x2
        x1 = c // 2
        x2 = c - x1

        c0 = c - c1 - c2
        if K < c0:
            y = c1 + c2 + K
            y1 = y // 2
            y2 = y - y1
            if c2 > y2:
                ans = c2 * (c1 + K)
            else:
                ans = y1 * y2
        else:
            K -= c0
            if c2 > x2:
                c1 += c0
                if c2 - c1 - 1 <= K * 2:
                    ans = x1 * x2
                else:
                    ans = (c2 - K) * (c1 + K)

            else:
                ans = x1 * x2
        print(ans)
