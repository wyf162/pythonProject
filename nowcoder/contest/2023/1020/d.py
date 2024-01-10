# -*- coding : utf-8 -*-
# @Time: 2023/10/20 20:49
# @Author: yefei.wang
# @File: d.py

import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

K = 1 << 20
tcn = I()
for _tcn_ in range(tcn):
    x = I()
    x %= K

    ans = 20
    for i in range(21):
        ans_i = i
        y = x + i
        y %= K
        while y:
            y *= 2
            y %= K
            ans_i += 1
        ans = min(ans, ans_i)
    print(ans)
