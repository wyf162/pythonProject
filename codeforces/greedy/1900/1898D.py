# -*- coding : utf-8 -*-
# @Time: 2023/11/19 23:18
# @Author: yefei.wang
# @File: C.py

import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    b = LI()
    ans = 0
    mx_left = 0
    mi_right = 0x3f3f3f3f
    for i in range(n):
        mi, mx = min(a[i], b[i]), max(a[i], b[i])
        if mi - mi_right > ans:
            ans = mi - mi_right
        if mx_left - mx > ans:
            ans = mx_left - mx
        if mi > mx_left:
            mx_left = mi
        if mx < mi_right:
            mi_right = mx
    ans += ans
    for i in range(n):
        ans += abs(a[i] - b[i])
    print(ans)
