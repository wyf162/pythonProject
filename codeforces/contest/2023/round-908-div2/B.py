# -*- coding : utf-8 -*-
# @Time: 2023/11/7 22:43
# @Author: yefei.wang
# @File: B.py
import sys
from collections import Counter

# sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    cnt = Counter(a)
    c = 0
    ks = []
    for k, v in cnt.items():
        if v >= 2:
            ks.append(k)
            c += 1
    if c < 2:
        print(-1)
        continue
    k1, k2 = ks[:2]
    res = [1] * n
    for i in range(n):
        if a[i] == k1:
            res[i] = 2
            break

    for i in range(n):
        if a[i] == k2:
            res[i] = 3
            break
    print(' '.join(map(str, res)))
