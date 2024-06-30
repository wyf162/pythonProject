# -*- coding : utf-8 -*-
# @Time: 2024/6/30 23:06
# @Author: yefei.wang
# @File: D.py

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
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
    A = LI()
    A.sort()
    print(A)
    cnt = Counter(A)
    cnt[5005] = 5005
    alice = 0
    while len(cnt) > 1:
        ks = list(sorted(cnt.keys()))
        alice += 1
        del cnt[ks.pop(0)]

        cur = 5005
        c1 = 1
        for k in ks:
            if cnt[k] <= c1 and cnt[k] < cnt[cur]:
                cur = k
            c1 += 1

        if cur < 5005:
            cnt[cur] -= 1
            if cnt[cur] == 0:
                del cnt[cur]

    print(alice)
