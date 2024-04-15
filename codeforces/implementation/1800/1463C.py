# -*- coding: utf-8 -*-
# @Time: 2024/4/15 14:35
# @Author: yfwang
# @File: 1463C.py
# https://codeforces.com/contest/1463/problem/C

import sys

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
    n = I()
    ops = [LI() for _ in range(n)]
    cur_location = 0
    cur_time = ops[0][0]
    nex_location = ops[0][1]
    target = ops[0][1]
    success = 0
    i = 1
    while i < n:
        while i < n and ops[i][0] - cur_time < abs(cur_location - nex_location):
            if cur_location < nex_location:
                now = cur_location + ops[i][0] - ops[i - 1][0]
                if cur_location <= target <= now:
                    success += 1
                cur_location = now
            else:
                now = cur_location - (ops[i][0] - ops[i - 1][0])
                if now <= target <= cur_location:
                    success += 1
                cur_location = now
            cur_time = ops[i][0]
            target = ops[i][1]
            i += 1
        if i < n:
            if cur_location <= nex_location and cur_location <= target <= nex_location:
                success += 1
            elif nex_location < cur_location and nex_location <= target <= cur_location:
                success += 1

            cur_time = ops[i][0]
            cur_location = nex_location
            nex_location = ops[i][1]
            target = ops[i][1]
            i += 1
    if cur_location <= nex_location and cur_location <= target <= nex_location:
        success += 1
    elif nex_location < cur_location and nex_location <= target <= cur_location:
        success += 1
    print(success)
