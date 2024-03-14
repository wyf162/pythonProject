# -*- coding : utf-8 -*-
# @Time: 2024/3/13 22:30
# @Author: yefei.wang
# @File: A.py

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
    s = input()
    cnt = 0
    mx = 0
    tot = 0
    for i, c in enumerate(s):
        if c == '1':
            tot += 1
            mx = max(mx, cnt)
            cnt = 0
        else:
            cnt += 1
    mx = max(mx, cnt)
    tot += mx
    print(tot)
