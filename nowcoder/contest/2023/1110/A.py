# -*- coding : utf-8 -*-
# @Time: 2023/11/10 19:03
# @Author: yefei.wang
# @File: B.py

import sys
from collections import Counter

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    t = input()
    ss = Counter(s)
    tt = Counter(t)
    ans = 10**5
    for k, v in tt.items():
        ans = min(ans, ss[k] // v)
    print(ans)
