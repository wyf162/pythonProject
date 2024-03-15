# -*- coding : utf-8 -*-
# @Time: 2024/1/3 22:47
# @Author: yefei.wang
# @File: 1748C.py

import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    zero_idxs = []
    for i in range(n):
        if a[i] == 0:
            zero_idxs.append(i)
    zero_idxs.append(n - 1)
    i0 = 0
    i = 0
    ans = 0
    while i < len(zero_idxs) - 1:
        i1 = zero_idxs[i]
        i2 = zero_idxs[i + 1]
        cnt = Counter()
        acc = 0
        cnt[acc] += 1
        for j in range(i1+1, i2):
            acc += a[j]
            cnt[acc] += 1
        mx = max(cnt.values())
        ans += mx
        i += 1

    print(ans)
