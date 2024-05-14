# -*- coding : utf-8 -*-
# @Time: 2023/10/11 0:19
# @Author: yefei.wang
# @File: 1359C.py

import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    h, c, t = MI()
    if t >= h:
        print(1)
        continue
    if t * 2 <= h + c:
        print(2)
        continue
    l, r = 0, 10 ** 7
    while l <= r:
        m = (l + r) // 2
        if (m + 1) * h + m * c >= (2 * m + 1) * t:
            l = m + 1
        else:
            r = m - 1
    if r >= 0 and abs(((r + 1) * h + r * c) * (2 * l + 1) - t * (2 * r + 1) * (2 * l + 1)) <= abs(
            ((l + 1) * h + l * c) * (2 * r + 1) - t * (2 * r + 1) * (2 * l + 1)):
        print(2 * r + 1)
    else:
        print(2 * l + 1)


