# -*- coding : utf-8 -*-
# @Time: 2024/4/23 20:41
# @Author: yefei.wang
# @File: 1775B.py

import sys
from collections import Counter

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
N = 200005

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    cnt = Counter()
    mtx = []
    for _ in range(n):
        row = LI()
        mtx.append(row)
    cnt = [0] * N
    for row in mtx:
        for x in row[1:]:
            cnt[x] += 1
    ans = False
    for row in mtx:
        if all(cnt[x] >= 2 for x in row[1:]):
            ans = True
            break
    YN(ans)
