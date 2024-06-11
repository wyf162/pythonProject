# -*- coding: utf-8 -*-
# @Time: 2024/6/11 10:55
# @Author: yfwang
# @File: 893D.py

import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = 1
for _tcn_ in range(tcn):
    n, d = MI()
    nums = LI()

    ans = 0
    l, r = 0, 0
    for num in nums:
        if num == 0:
            l = max(l, 0)
            if r < 0:
                r = d
                ans += 1
        else:
            l += num
            r += num
            r = min(r, d)
            if l > d:
                print(-1)
                exit()

    print(ans)
