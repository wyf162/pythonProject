# -*- coding : utf-8 -*-
# @Time: 2023/9/26 22:41
# @Author: yefei.wang
# @File: b.py

import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()

for _tcn_ in range(tcn):
    n = I()
    ans = [i * 2 + 1 for i in range(n)]
    print(' '.join(map(str, ans)))
