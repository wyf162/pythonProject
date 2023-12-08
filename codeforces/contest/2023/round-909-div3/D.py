# -*- coding : utf-8 -*-
# @Time: 2023/11/17 23:01
# @Author: yefei.wang
# @File: D.py
import math
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
    cnt = Counter()
    for x in a:
        if x in [1, 2]:
            cnt[2] += 1
        else:
            cnt[x] += 1
    ans = 0
    for k, v in cnt.items():
        ans += math.comb(v, 2)
    print(ans)

