# -*- coding: utf-8 -*-
# @Time: 2024/7/23 14:41
# @Author: yfwang
# @File: 1902D.py

import bisect
import sys
from collections import defaultdict

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

tcn = 1
for _tcn_ in range(tcn):
    n, q = MI()
    path = list(input())
    cur = (0, 0)
    hst1 = defaultdict(list)
    coords = [cur]
    for i, direction in enumerate(path):
        x, y = cur
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        cur = (x, y)
        hst1[cur].append(i + 1)
        coords.append(cur)


    def check(x, y, l, r):
        A = hst1[(x, y)]
        i = bisect.bisect_left(A, l)
        return A[i] <= r if i < len(A) else False


    outs = []
    for _ in range(q):
        x, y, L, R = MI()
        ans = False
        ans |= check(x, y, 0, L - 1)
        ans |= check(x, y, R, n)
        nx, ny = coords[R][0] + coords[L - 1][0] - x, coords[R][1] + coords[L - 1][1] - y
        ans |= check(nx, ny, L, R - 1)

        outs.append('YES' if ans else "NO")

    print("\n".join(outs))
    print()
