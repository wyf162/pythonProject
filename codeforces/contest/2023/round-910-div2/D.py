# -*- coding : utf-8 -*-
# @Time: 2023/11/19 23:18
# @Author: yefei.wang
# @File: D.py

import math
import sys

sys.stdin = open('./../../../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    b = LI()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b[i])
    a_great_b_a = []
    a_great_b_b = []
    a_less_b_a = []
    a_less_b_b = []
    for i in range(n):
        if a[i] - b[i] > 0:
            a_great_b_a.append(a[i])
            a_great_b_b.append(b[i])
        elif a[i] - b[i] < 0:
            a_less_b_a.append(a[i])
            a_less_b_b.append(b[i])
        else:
            a_great_b_a.append(a[i])
            a_great_b_b.append(b[i])
            a_less_b_a.append(a[i])
            a_less_b_b.append(b[i])
    mx_df1, mx_df2, mx_df3, mx_df4 = 0, 0, 0, 0
    if a_less_b_b and a_less_b_a:
        mx_df1 = 2 * (max(a_less_b_a) - min(a_less_b_b))

    # if a_less_b_a and a_great_b_b:
    #     mx_df2 = 2 * (max(a_great_b_b) - min(a_less_b_a))

    if a_great_b_a and a_less_b_a:
        mx_df3 = 2 * (max(a_less_b_a) - min(a_great_b_a))

    if a_less_b_b and a_great_b_b:
        mx_df4 = 2 * (max(a_great_b_b) - min(a_less_b_b))

    ans += max(mx_df1, mx_df2, mx_df3, mx_df4)
    print(ans)
