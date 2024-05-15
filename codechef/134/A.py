# -*- coding : utf-8 -*-
# @Time: 2024/5/15 22:27
# @Author: yefei.wang
# @File: A.py

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
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = input()
    nums = []
    # R > S 0 > 1
    # S > P 1 > 2
    # P > R 2 > 0
    for c in s:
        if c == 'R':
            nums.append(0)
        elif c == 'S':
            nums.append(1)
        elif c == 'P':
            nums.append(2)
    f = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(n):
        if nums[i] == 0:
            f[i + 1][2] = max(f[i][1], f[i][0]) + 1
            f[i + 1][1] = max(f[i][0], f[i][2])
            f[i + 1][0] = max(f[i][1], f[i][2])

        if nums[i] == 1:
            f[i + 1][0] = max(f[i][1], f[i][2]) + 1
            f[i + 1][1] = max(f[i][0], f[i][2])
            f[i + 1][2] = max(f[i][0], f[i][1])

        if nums[i] == 2:
            f[i + 1][1] = max(f[i][0], f[i][2]) + 1
            f[i + 1][0] = max(f[i][1], f[i][2])
            f[i + 1][2] = max(f[i][0], f[i][1])
    ans = max(f[n])
    print(ans)
